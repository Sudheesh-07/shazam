#!/usr/bin/env python3
"""
Installation script for Shazam CLI tool
Creates dynamic command based on user preference
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def create_dynamic_command(command_name: str):
    """Create a dynamic command script"""
    
    # Create the command script
    script_content = f'''#!/usr/bin/env python3
"""
Dynamic command script for {command_name}
"""

import sys
from shazam.cli import main

if __name__ == '__main__':
    sys.argv[0] = '{command_name}'
    main()
'''
    
    # Find appropriate bin directory
    if os.name == 'nt':  # Windows
        # Use Scripts directory in virtual environment or user directory
        if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
            bin_dir = Path(sys.prefix) / 'Scripts'
        else:
            bin_dir = Path.home() / 'AppData' / 'Local' / 'Programs' / 'Python' / 'Scripts'
        
        script_path = bin_dir / f'{command_name}.py'
        
    else:  # Unix-like systems
        # Try to use virtual environment first, then system paths
        if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
            bin_dir = Path(sys.prefix) / 'bin'
        else:
            # Check for user bin directory
            user_bin = Path.home() / '.local' / 'bin'
            if user_bin.exists():
                bin_dir = user_bin
            else:
                bin_dir = Path('/usr/local/bin')
        
        script_path = bin_dir / command_name
    
    # Ensure bin directory exists
    bin_dir.mkdir(parents=True, exist_ok=True)
    
    # Write the script
    try:
        with open(script_path, 'w') as f:
            f.write(script_content)
        
        # Make executable on Unix-like systems
        if os.name != 'nt':
            os.chmod(script_path, 0o755)
        
        print(f"✅ Command '{command_name}' created at: {script_path}")
        
        # Check if bin directory is in PATH
        if str(bin_dir) not in os.environ.get('PATH', ''):
            print(f"⚠️  Warning: {bin_dir} is not in your PATH")
            print(f"   Add this to your shell configuration:")
            print(f"   export PATH=\"{bin_dir}:$PATH\"")
        
        return True
        
    except PermissionError:
        print(f"❌ Permission denied writing to {script_path}")
        print("   Try running with sudo or choose a different location")
        return False
    except Exception as e:
        print(f"❌ Error creating command script: {e}")
        return False

def install_shazam():
    """Main installation function"""
    print("🚀 Installing Shazam CLI Tool...")
    print()
    
    # Install the package
    try:
        print("📦 Installing Python package...")
        result = subprocess.run([
            sys.executable, '-m', 'pip', 'install', '-e', '.'
        ], check=True, capture_output=True, text=True)
        print("✅ Package installed successfully!")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install package: {e}")
        print(f"Error output: {e.stderr}")
        return False
    
    # Import and setup configuration
    try:
        from shazam.config import Config
        config = Config()
        
        if config.setup_wizard():
            command_name = config.get('command_name', 'jarvis')
            
            # Offer shell integration
            # print()
            # if input(f"Install shell integration for better readline experience? (Y/n): ").lower() != 'n':
            #     try:
            #         from shazam.shell_integration import install_shell_function
            #         install_shell_function()
            #         print()
            #         print("🎉 Installation completed successfully with shell integration!")
            #         print(f"💡 Restart your shell and try: {command_name} 'list files'")
            #         print(f"💡 The command will appear on your prompt line - just press Enter!")
            #         print(f"💡 For auto-execution: {command_name} -r 'show disk usage'")
            #         return True
            #     except Exception as e:
            #         print(f"⚠️  Shell integration failed: {e}")
            #         print("   You can install it later with: python -m shazam --install-shell")
            
            # Create dynamic command as fallback
            if create_dynamic_command(command_name):
                print()
                print("🎉 Installation completed successfully!")
                print(f"💡 Your AI assistant is ready! Try: {command_name} 'list files'")
                print(f"💡 For auto-execution: {command_name} -r 'show disk usage'")
                print(f"💡 To install shell integration: {command_name} --install-shell")
                print(f"💡 To reconfigure: {command_name} --setup")
                return True
            else:
                print("⚠️  Package installed but command creation failed")
                print("   You can still use: python -m shazam")
                return True
                
    except Exception as e:
        print(f"❌ Error during setup: {e}")
        print("   You can run setup later with: python -m shazam --setup")
        return False

if __name__ == '__main__':
    success = install_shazam()
    sys.exit(0 if success else 1)