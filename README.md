# ⚡ Shazam CLI - AI-Powered Bash Command Generator

Transform natural language into bash commands using your own GGUF model!

## To use the tool you need to download and load the model in models/ directory 
### To know how to download and use the model refer to [MODEL_GUIDE.md](MODEL_GUIDE.md)

## 📁 Project Structure

```
shazam-cli/
├── shazam/                # Main package
│   ├── models/                # Directory where your model should be
│        └──download_link.txt   # Drive link to download the model 
│   ├── __init__.py        # Package init
│   ├── cli.py             # CLI interface
│   ├── config.py          # Configuration management
│   └── model.py           # GGUF model interface
├── install.py             # Installation script
├── setup.py               # Package setup
├── requirements.txt       # Dependencies
├── .gitignore             # Git ignore rules
├── LICENSE                # MIT license 
├── README.md              # Main documentation
├── MODEL_GUIDE.md         # Model setup guide
└── CONTRIBUTING.md        # This file
```

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

1. **First Run (Optional)**: The setup wizard will guide you through configuration
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
command_name: your_assistant_name
model_params:
  max_tokens: 150
  stop_sequences:
  - '


    '
  - '```'
  temperature: 0.1
  top_p: 0.9
model_path: path/to/your/model.gguf
safety:
  dangerous_commands:
  - rm -rf /
  - mkfs
  - dd if=
  - shutdown
  - reboot
  - halt
  - sudo rm
  - chmod 777 /
  require_confirmation: true
```