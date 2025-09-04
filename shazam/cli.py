#!/usr/bin/env python3
"""
Main CLI interface for Shazam
"""

import os
import sys
import subprocess
import click
from colorama import init, Fore, Style
from .config import Config
from .model import ModelInterface

# Initialize colorama for cross-platform colored output
init(autoreset=True)

class ShazamCLI:
    def __init__(self):
        self.config = Config()
        self.model = None
        self._load_model()
    
    def _load_model(self):
        """Load the AI model"""
        if self.config.is_first_run():
            return  # Model will be loaded after setup
        
        model_path = self.config.get('model_path')
        if not model_path or not os.path.exists(model_path):
            print(f"{Fore.RED}Model file not found. Please run setup again.{Style.RESET_ALL}")
            return
        
        try:
            model_params = self.config.get('model_params', {})
            self.model = ModelInterface(model_path, **model_params)
        except Exception as e:
            print(f"{Fore.RED}Failed to load model: {e}{Style.RESET_ALL}")
            sys.exit(1)
    
    def generate_command(self, prompt: str) -> str:
        """Generate bash command from prompt"""
        if not self.model:
            print(f"{Fore.RED}Model not loaded. Please check your configuration.{Style.RESET_ALL}")
            return ""
        
        print(f"{Fore.YELLOW}Thinking...{Style.RESET_ALL}")
        
        try:
            command = self.model.generate_command(
                prompt,
                max_tokens=self.config.get('model_params.max_tokens', 150),
                temperature=self.config.get('model_params.temperature', 0.1),
                top_p=self.config.get('model_params.top_p', 0.9),
                stop_sequences=self.config.get('model_params.stop_sequences')
            )
            
            if not command:
                print(f"{Fore.RED}Could not generate command for: {prompt}{Style.RESET_ALL}")
                return ""
            
            return command
            
        except Exception as e:
            print(f"{Fore.RED}Error generating command: {e}{Style.RESET_ALL}")
            return ""
    
    def is_safe_command(self, command: str) -> bool:
        """Check if command is safe to execute"""
        dangerous_commands = self.config.get('safety.dangerous_commands', [])
        
        if self.model.is_dangerous_command(command, dangerous_commands):
            return False
        
        return True
    
    def execute_command(self, command: str, auto_run: bool = False) -> bool:
        """Execute the generated command"""
        if not command:
            return False
        
        # Safety check
        if not self.is_safe_command(command):
            print(f"{Fore.RED}⚠️  Potentially dangerous command detected: {command}{Style.RESET_ALL}")
            if not click.confirm(f"{Fore.YELLOW}Do you want to proceed anyway?{Style.RESET_ALL}"):
                print(f"{Fore.BLUE}Command cancelled for safety.{Style.RESET_ALL}")
                return False
        
        # Show the command
        print(f"{Fore.GREEN}Generated command:{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{command}{Style.RESET_ALL}")
        
        if auto_run:
            print(f"{Fore.YELLOW}Executing automatically...{Style.RESET_ALL}")
            execute = True
        else:
            # Ask for confirmation unless auto-run is enabled
            print(f"\n{Fore.YELLOW}Press Enter to execute, Ctrl+C to cancel")
            try:
                user_input = input().strip()
                # if user_input.lower() == 'e':
                #     command = input(f"{Fore.CYAN}Edit command: {Style.RESET_ALL}") or command
                #     print(f"{Fore.GREEN}Updated command: {command}{Style.RESET_ALL}")
                execute = True
            except KeyboardInterrupt:
                print(f"\n{Fore.BLUE}Command cancelled.{Style.RESET_ALL}")
                return False
        
        if execute:
            try:
                # Execute the command
                result = subprocess.run(
                    command,
                    shell=True,
                    capture_output=False,
                    text=True
                )
                
                if result.returncode == 0:
                    print(f"{Fore.GREEN}✅ Command executed successfully!{Style.RESET_ALL}")
                else:
                    print(f"{Fore.YELLOW}⚠️  Command exited with code: {result.returncode}{Style.RESET_ALL}")
                
                return True
                
            except Exception as e:
                print(f"{Fore.RED}❌ Error executing command: {e}{Style.RESET_ALL}")
                return False
        
        return False

# Create a global instance
shazam_cli = ShazamCLI()

@click.command()
@click.argument('prompt', required=False)
@click.option('-r', '--run', is_flag=True, help='Automatically execute the generated command')
@click.option('--setup', is_flag=True, help='Run the setup wizard')
@click.option('--config', help='Show or set configuration values')
def main(prompt, run, setup, config):
    """
    🚀 Shazam - AI-powered bash command generator
    
    Convert natural language to bash commands using AI.
    
    Examples:
        shazam "list all python files"
        shazam -r "show disk usage"
        shazam --setup
    """
    
    # Handle setup
    if setup or shazam_cli.config.is_first_run():
        if shazam_cli.config.setup_wizard():
            shazam_cli._load_model()  # Reload model after setup
        return
    
    # Handle config display/modification
    if config:
        if '=' in config:
            key, value = config.split('=', 1)
            try:
                # Try to convert value to appropriate type
                if value.lower() in ['true', 'false']:
                    value = value.lower() == 'true'
                elif value.isdigit():
                    value = int(value)
                elif '.' in value and value.replace('.', '').isdigit():
                    value = float(value)
                
                shazam_cli.config.set(key.strip(), value)
                print(f"{Fore.GREEN}✅ Configuration updated: {key} = {value}{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}❌ Error setting configuration: {e}{Style.RESET_ALL}")
        else:
            value = shazam_cli.config.get(config)
            print(f"{Fore.CYAN}{config}: {value}{Style.RESET_ALL}")
        return
    
    # Check if we have a prompt
    if not prompt:
        print(f"{Fore.RED}❌ Please provide a prompt or use --help for usage information{Style.RESET_ALL}")
        return
    
    # Generate and execute command
    command = shazam_cli.generate_command(prompt)
    if command:
        shazam_cli.execute_command(command, auto_run=run)

if __name__ == '__main__':
    main()