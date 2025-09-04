# 🚀 Shazam CLI - AI-Powered Bash Command Generator

Transform natural language into bash commands using your own GGUF model!

## ✨ Features

- 🤖 **AI-Powered**: Uses your local GGUF model to generate bash commands
- 🎯 **Smart & Safe**: Built-in safety checks for dangerous commands
- 🚀 **Auto-Execute**: Optional flag to run commands immediately
- 🎨 **Customizable**: Choose your own command name (jarvis, friday, cortana, etc.)
- 🔧 **Configurable**: Adjust model parameters and safety settings
- 🌈 **User-Friendly**: Colored output and intuitive interface

## 📋 Requirements

- Python 3.8+
- A GGUF model file (compatible with llama.cpp)
- Sufficient RAM to run your chosen model

## 🛠️ Installation

### Quick Install

```bash
git clone <your-repo>
cd shazam-cli
python install.py
```

### Manual Install

```bash
# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .

# Run setup
python -m shazam --setup
```

## 🚀 Quick Start

1. **First Run**: The setup wizard will guide you through configuration
   ```bash
   shazam --setup
   ```

2. **Basic Usage**: Generate commands from natural language
   ```bash
   jarvis "list all python files"
   # Output: find . -name "*.py"
   # Press Enter to execute, Ctrl+C to cancel
   ```

3. **Auto-Execute**: Use `-r` flag to run commands immediately
   ```bash
   jarvis -r "show disk usage"
   # Automatically runs: df -h
   ```

4. **Edit Before Execution**: Type 'e' when prompted to edit the command
   ```bash
   jarvis "delete all log files"
   # Generated: find . -name "*.log" -delete
   # Type 'e' to edit before execution
   ```

## 💡 Usage Examples

```bash
# File operations
jarvis "find large files bigger than 100MB"
jarvis "count lines in all Python files"
jarvis "compress folder documents to zip"

# System monitoring
jarvis -r "show running processes"
jarvis -r "check memory usage"
jarvis -r "display network connections"

# Git operations
jarvis "show git status and recent commits"
jarvis "create new branch feature-x"

# Text processing
jarvis "find TODO comments in code"
jarvis "replace tabs with spaces in all files"
```

## ⚙️ Configuration

### View Configuration
```bash
jarvis --config model_path
jarvis --config command_name
```

### Modify Configuration
```bash
jarvis --config "command_name=friday"
jarvis --config "model_params.temperature=0.2"
jarvis --config "model_params.max_tokens=200"
```

### Configuration File
The configuration is stored at `~/.shazam/config.yaml`:

```yaml
model_path: "/path/to/your/model.gguf"
command_name: "jarvis"
model_params:
  max_tokens: 150
  temperature: 0.