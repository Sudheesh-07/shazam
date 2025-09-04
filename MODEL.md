# 🤖 Model Setup Guide for Shazam CLI

Shazam requires a GGUF model to function. **We recommend using our fine-tuned model** specifically trained for bash command generation, but you can also use other compatible models.

## 🎯 Recommended Model (Fine-tuned for Shazam)

**Phi-3-mini-4k-instruct Fine-tuned for Bash Command Generation**

I have fine-tuned Microsoft's Phi-3-mini-4k-instruct model using the [NL2Bash dataset](https://github.com/TellinaTool/nl2bash) and [NL2CMD](https://huggingface.co/datasets/TRamesh2/NL2CMD)to specifically excel at converting natural language to bash commands.

### Download Our Fine-tuned Model
**File Size**: ~2.1GB | **RAM Required**: 2-4GB | **Optimized for**: Command Generation

```bash
# Navigate to the models directory
cd shazam/models/

# Download the fine-tuned model (check download_link.txt for the current URL)
```
It is a google drive link where you can download the model

> 📁 **Important**: The model MUST be placed in the `models/` folder in the project root directory, otherwise Shazam won't work properly.

### Why This Model is Better
- ✅ **Specifically trained** on bash command generation tasks 
- ✅ **Optimized prompting** - understands the exact format needed
- ✅ **Smaller size** while maintaining quality

## 🏗️ Model Training Details

Our fine-tuning process:
- **Base Model**: [Microsoft Phi-3-mini-4k-instruct](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct)
- **Dataset**: [NL2Bash Dataset](https://github.com/TellinaTool/nl2bash) and [NL2CMD](https://huggingface.co/datasets/TRamesh2/NL2CMD) - 19,657 English sentence and bash command pairs
- **Quantization**: 4-bit BNB quantization for optimal size/performance balance
- **Fine-tuning**: Specialized on natural language → bash command translation tasks
- **Validation**: Tested on diverse command generation scenarios

The NL2Bash dataset contains pairs like:
- "Change directory to My desktop" → `cd home/MyDesktop`
- "find all python files" → `find . -name "*.py"`
- "show disk usage" → `df -h`

## 📁 Required Directory Structure

```
shazam-cli/
├── models/                    # ← Model MUST go here
│   ├── download_links.txt     # Download URLs
│   └── phi3-mini-nl2bash-finetuned.gguf  # ← Your downloaded model
├── shazam/
├── setup.py
└── ...
```

## 🚀 Quick Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/shazam-cli.git
   cd shazam-cli
   ```

2. **Download the recommended model**:
   ```bash
   # Check the models/download_links.txt file for the current download URL
   cd models/
   cat download_links.txt  # Shows the download URL
    ```

3. **Install and setup**:
   ```bash
   python install.py
   ```

## 🔄 Alternative Models (If You Want to Experiment)

If you prefer to use other models, here are some alternatives:

### For Most Users (8GB+ RAM)
**Llama 2 7B Chat GGUF (Q4_K_M)** - ~4GB
```bash
# Download using wget
wget https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q4_K_M.gguf

# Or using curl
curl -L -o llama-2-7b-chat.Q4_K_M.gguf https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q4_K_M.gguf
```

### For Lower RAM Systems (4-8GB RAM)
**Llama 2 7B Chat GGUF (Q3_K_M)** - ~2.9GB
```bash
wget https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q3_K_M.gguf
```

### For High-Performance Systems (16GB+ RAM)
**Code Llama 7B Instruct GGUF (Q4_K_M)** - ~4GB (Better for coding tasks)
```bash
wget https://huggingface.co/TheBloke/CodeLlama-7B-Instruct-GGUF/resolve/main/codellama-7b-instruct.Q4_K_M.gguf
```

## 📁 Model Directory Structure

Create a dedicated directory for your models:
```bash
mkdir ~/shazam-models
cd ~/shazam-models

# Download your chosen model here
wget [model-url]
```

## 🔧 Alternative Download Methods

### Using Hugging Face Hub
```bash
pip install huggingface_hub
python -c "
from huggingface_hub import hf_hub_download
hf_hub_download(
    repo_id='TheBloke/Llama-2-7B-Chat-GGUF',
    filename='llama-2-7b-chat.Q4_K_M.gguf',
    local_dir='./models'
)
"
```

### Using Git LFS (for any HuggingFace model)
```bash
# Install git-lfs if not already installed
git lfs install

# Clone specific model repo
git clone https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF
cd Llama-2-7B-Chat-GGUF

# Download specific file
git lfs pull --include="llama-2-7b-chat.Q4_K_M.gguf"
```

## 🎯 Model Recommendations by Use Case

### General Command Generation
- **Llama 2 7B Chat**: Best balance of performance and size
- **Mistral 7B Instruct**: Fast and efficient
- **Zephyr 7B Beta**: Good instruction following

### Coding-Specific Tasks
- **Code Llama 7B Instruct**: Specialized for code generation
- **WizardCoder 7B**: Strong coding capabilities
- **DeepSeek Coder 6.7B**: Excellent for shell commands

### Resource-Constrained Systems
- **TinyLlama 1.1B Chat**: Very lightweight (~600MB)
- **Phi-2 2.7B**: Microsoft's efficient model
- **StableLM 3B**: Good performance for size

## 📊 Model Size Guide

| Quantization | File Size | RAM Usage | Quality | Speed |
|-------------|-----------|-----------|---------|-------|
| Q2_K        | ~2.3GB    | ~4GB      | Lower   | Fast  |
| Q3_K_M      | ~2.9GB    | ~5GB      | Good    | Fast  |
| Q4_K_M      | ~4.0GB    | ~6GB      | High    | Med   |
| Q5_K_M      | ~4.8GB    | ~7GB      | Higher  | Slow  |
| Q8_0        | ~7.0GB    | ~9GB      | Highest | Slow  |

## 🛠️ Setup Process

1. **Download Model**: Choose and download a model using methods above
2. **Install Shazam**: `python install.py`
3. **Run Setup**: The setup wizard will ask for your model path
4. **Test**: Try `jarvis "list files"` to test

## 🔍 Finding More Models

### Popular Sources
- **Hugging Face**: https://huggingface.co/models?library=gguf
- **TheBloke's Models**: https://huggingface.co/TheBloke (Pre-quantized GGUF models)
- **Ollama Library**: https://ollama.ai/library (Can convert to GGUF)

### Search Tips
- Look for "GGUF" in model names
- Check model cards for RAM requirements
- Q4_K_M is usually the best balance
- Instruct/Chat models work better than base models

## 🚨 Troubleshooting

### Model Loading Issues
```bash
# Check if file exists and is readable
ls -la /path/to/your/model.gguf

# Verify it's a valid GGUF file
file /path/to/your/model.gguf
```

### Memory Issues
- Try a smaller quantization (Q3_K_M instead of Q4_K_M)
- Reduce `n_ctx` in config: `jarvis --config "model_params.n_ctx=1024"`
- Close other applications to free RAM

## 📝 Model Configuration

After setup, you can adjust model parameters:
```bash
# View current config
jarvis --config model_path

# Adjust parameters
jarvis --config "model_params.temperature=0.3"
jarvis --config "model_params.max_tokens=100"
jarvis --config "model_params.top_p=0.8"
```

## 🤝 Contributing Models

If you find a model that works particularly well for command generation, please:
1. Test it thoroughly with various prompts
2. Note RAM requirements and performance
3. Share your findings in the project issues
4. Update this guide with your recommendations

---

**Need help?** Open an issue on GitHub with:
- Your system specs (RAM, CPU, GPU)
- Model you're trying to use
- Error messages (if any)