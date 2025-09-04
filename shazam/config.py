#!/usr/bin/env python3
"""
Configuration management for Shazam CLI tool
"""

import os
import yaml
import json
from pathlib import Path
from typing import Dict, Any, Optional

class Config:
    def __init__(self):
        self.config_dir = Path.home() / '.shazam'
        self.config_file = self.config_dir / 'config.yaml'
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file or create default"""
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                return yaml.safe_load(f) or {}
        else:
            return self._create_default_config()
    
    def _create_default_config(self) -> Dict[str, Any]:
        """Create default configuration"""
        return {
            'model_path': '',
            'command_name': 'jarvis',
            'model_params': {
                'max_tokens': 150,
                'temperature': 0.1,
                'top_p': 0.9,
                'stop_sequences': ['\n\n', '```']
            },
            'safety': {
                'dangerous_commands': [
                    'rm -rf /',
                    'mkfs',
                    'dd if=',
                    'shutdown',
                    'reboot',
                    'halt',
                    'sudo rm',
                    'chmod 777 /'
                ],
                'require_confirmation': True
            }
        }
    
    def save_config(self):
        """Save current configuration to file"""
        self.config_dir.mkdir(exist_ok=True)
        with open(self.config_file, 'w') as f:
            yaml.dump(self.config, f, default_flow_style=False, indent=2)
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value"""
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        return value
    
    def set(self, key: str, value: Any):
        """Set configuration value"""
        keys = key.split('.')
        config = self.config
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        config[keys[-1]] = value
        self.save_config()
    
    def is_first_run(self) -> bool:
        """Check if this is the first run"""
        return not self.config_file.exists() or not self.get('model_path')
    
    def setup_wizard(self):
        """Interactive setup wizard for first-time configuration"""
        print("🚀 Welcome to Shazam CLI Setup!")
        print("Let's configure your AI assistant...")
        print()
        
        # Get model path
        while True:
            model_path = "models/unsloth.Q4_K_M.gguf"
            if not model_path:
                print("❌ Model path cannot be empty!")
                continue
                
            model_path = os.path.expanduser(model_path)
            if not os.path.exists(model_path):
                print(f"❌ Model file not found: {model_path}")
                continue
                
            if not model_path.endswith(('.gguf', '.ggml')):
                print("⚠️  Warning: File doesn't have .gguf extension. Continue? (y/n)", end=' ')
                if input().lower() != 'y':
                    continue
            
            self.set('model_path', model_path)
            print(f"✅ Model path set: {model_path}")
            break
        
        # Get command name
        print()
        current_name = self.get('command_name', 'jarvis')
        command_name = input(f"🤖 Enter your assistant's name (current: {current_name}): ").strip()
        if command_name:
            self.set('command_name', command_name)
            print(f"✅ Assistant name set: {command_name}")
        
        # Optional: Model parameters
        print("🔧 Advanced settings (press Enter to use defaults):")
        
        max_tokens = input(f"Max tokens ({self.get('model_params.max_tokens')}): ").strip()
        if max_tokens and max_tokens.isdigit():
            self.set('model_params.max_tokens', int(max_tokens))
        
        temperature = input(f"Temperature ({self.get('model_params.temperature')}): ").strip()
        if temperature:
            try:
                temp = float(temperature)
                if 0 <= temp <= 2:
                    self.set('model_params.temperature', temp)
            except ValueError:
                pass
        
        print()
        print("🎉 Setup complete! You can now use your assistant.")
        print(f"💡 Try: {self.get('command_name')} 'list files in current directory'")
        print(f"💡 Or with auto-run: {self.get('command_name')} -r 'show disk usage'")
        
        return True