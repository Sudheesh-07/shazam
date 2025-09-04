#!/usr/bin/env python3
"""
GGUF model interface for Shazam CLI tool
"""

import re
import os
from typing import Optional, List
from llama_cpp import Llama

class ModelInterface:
    def __init__(self, model_path: str, **kwargs):
        """Initialize the GGUF model"""
        self.model_path = model_path
        self.model = None
        self.model_params = kwargs
        self._load_model()
    
    def _load_model(self):
        """Load the GGUF model"""
        try:
            # Default parameters for GGUF models
            default_params = {
                'n_ctx': 2048,
                'n_threads': os.cpu_count(),
                'n_gpu_layers': -1,  # Use GPU if available
                'verbose': False
            }
            
            # Merge with user-provided parameters
            params = {**default_params, **self.model_params}
            
            self.model = Llama(
                model_path=self.model_path,
                **params
            )
            print("✅ Model loaded successfully!")
            
        except Exception as e:
            print(f"❌ Error loading model: {e}")
            raise
    
    def generate_command(self, prompt: str, max_tokens: int = 150, 
                        temperature: float = 0.1, top_p: float = 0.9,
                        stop_sequences: Optional[List[str]] = None) -> str:
        """Generate bash command from natural language prompt"""
        
        if not self.model:
            raise RuntimeError("Model not loaded")
        
        # Create a focused system prompt for bash command generation
        system_prompt = """You are a helpful AI assistant that converts natural language requests into bash commands. 

Rules:
- Return ONLY the bash command, nothing else
- No explanations or comments
- No markdown formatting or backticks
- One command per line
- Use common Unix/Linux commands
- Be safe and practical

Examples:
User: list files in current directory
Assistant: ls -la

User: show disk usage
Assistant: df -h

User: find all python files
Assistant: find . -name "*.py"

User: """

        # Combine system prompt with user prompt
        full_prompt = system_prompt + prompt + "\nAssistant: "
        
        try:
            # Generate response
            response = self.model(
                full_prompt,
                max_tokens=max_tokens,
                temperature=temperature,
                top_p=top_p,
                stop=stop_sequences or ['\n\n', 'User:', 'Assistant:'],
                echo=False
            )
            
            # Extract the generated text
            generated_text = response['choices'][0]['text'].strip()
            
            # Clean up the response
            command = self._clean_command(generated_text)
            
            return command
            
        except Exception as e:
            print(f"Error generating command: {e}")
            return ""
    
    def _clean_command(self, raw_command: str) -> str:
        """Clean and validate the generated command"""
        # Remove any markdown formatting
        command = re.sub(r'```.*?```', '', raw_command, flags=re.DOTALL)
        command = re.sub(r'`([^`]+)`', r'\1', command)
        
        # Remove common prefixes/suffixes
        prefixes_to_remove = [
            'bash:', 'shell:', 'command:', '$', '# ',
            'Here\'s the command:', 'The command is:',
            'You can use:', 'Try this:'
        ]
        
        for prefix in prefixes_to_remove:
            if command.lower().startswith(prefix.lower()):
                command = command[len(prefix):].strip()
        
        # Take only the first line if multiple lines exist
        command = command.split('\n')[0].strip()
        
        # Remove any trailing explanations
        if ' #' in command:
            command = command.split(' #')[0].strip()
        
        return command
    
    def is_dangerous_command(self, command: str, dangerous_patterns: List[str]) -> bool:
        """Check if a command contains dangerous patterns"""
        command_lower = command.lower()
        
        for pattern in dangerous_patterns:
            if pattern.lower() in command_lower:
                return True
                
        # Additional safety checks
        dangerous_chars = ['&&', '||', ';', '|']
        if any(char in command for char in dangerous_chars):
            # Allow safe piping but be cautious with chaining
            if not any(safe_pipe in command for safe_pipe in ['| grep', '| head', '| tail', '| sort', '| wc']):
                return True
        
        return False
    
    def __del__(self):
        """Cleanup"""
        if hasattr(self, 'model') and self.model:
            del self.model