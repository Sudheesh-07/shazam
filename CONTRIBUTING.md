# 🤝 Contributing to Shazam CLI

Thanks for your interest in contributing! This guide will help you get started.

## 🚀 Quick Start for Contributors

1. **Fork the repository** on GitHub
2. **Clone your fork**:
   ```bash
   git clone https://github.com/yourusername/shazam-cli.git
   cd shazam-cli
   ```
3. **Set up development environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   pip install -e .
   ```
4. **Download a test model** (see [MODEL_GUIDE.md](MODEL_GUIDE.md))

## 🎯 How to Contribute

### 🐛 Reporting Bugs
- Use the GitHub Issues tab
- Include system info (OS, Python version, shell)
- Include model info (name, size, quantization)
- Provide reproduction steps
- Include error messages/logs

### 💡 Suggesting Features
- Check existing issues first
- Describe the use case clearly
- Explain why it would be beneficial
- Consider implementation complexity

### 🔧 Code Contributions

#### Areas We Need Help With:
1. **Model's output in readline**: Currently the output is getting printed and waiting for user input. Looking for contributions on how to bring the input to directly on the shell's readline
2. **Shell Support**: PowerShell, CMD, other shells
3. **Safety Features**: Better command validation
4. **Performance**: Faster model loading, caching
5. **UI/UX**: Better error messages, help text
6. **Testing**: Unit tests, integration tests
7. **Documentation**: Examples, tutorials



#### Pull Request Process:
1. **Create a branch**: `git checkout -b feature/your-feature-name`
2. **Make your changes**
3. **Test thoroughly**:
   ```bash
   # Test basic functionality
   python -m shazam --setup
   python -m shazam "test command generation"

   ```
4. **Commit with clear messages**:
   ```bash
   git commit -m "feat: add support for PowerShell integration"
   git commit -m "fix: handle model loading timeout gracefully"
   ```
5. **Push and create PR**:
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Fill out PR template** with description and testing info


## 📁 Project Structure

```
shazam-cli/
├── models/                # Directory where your model should be
│   └──download_link.txt   # Drive link to download the model 
├── shazam/                # Main package
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

## 🔧 Development Tips

### Working with Models:
- Use smaller models for development (Q3_K_M or Q2_K)
- Test with different model sizes to ensure compatibility
- Consider model loading time in UX design

### Safety Features:
- Always err on the side of caution
- Test dangerous command detection thoroughly
- Consider false positives vs false negatives


## 📝 Documentation

### When Adding Features:
1. Update relevant docstrings
2. Add examples to README if user-facing
3. Update MODEL_GUIDE.md if model-related
4. Add configuration options to help text

### Documentation Style:
- Use clear, concise language
- Include practical examples
- Consider different skill levels
- Test all examples



## ❓ Questions?

- **General questions**: Open a GitHub Discussion
- **Bug reports**: Open a GitHub Issue
- **Feature requests**: Open a GitHub Issue with enhancement label
- **Development questions**: Feel free to open a draft PR for discussion

## 📜 Code of Conduct

- Be respectful and inclusive
- Help others learn and grow
- Focus on constructive feedback
- Welcome newcomers warmly

Thank you for contributing to Shazam CLI! 🚀