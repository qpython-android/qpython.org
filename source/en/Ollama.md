# Ollama - Local Large Language Model Integration

Ollama is a local large language model runtime framework that supports a variety of models including Deepseek, Qwen, and Gemma. QPython has built-in Ollama integration, enabling developers to explore GenAI development directly on their mobile devices.

![Ollama](static/ollama_demo.jpg)

## Overview

Ollama allows you to run powerful large language models locally on your Android device. With QPython's integration, you can:

- Run open-source LLMs directly on your phone
- Use AI capabilities without internet connectivity
- Experiment with different models for various use cases
- Build AI-powered applications using familiar Python libraries

## Supported Models

Ollama supports many popular open-source models:

- **Deepseek** – Efficient reasoning models (recommended: deepseek-r1:1.5b for mobile)
- **Qwen** – Alibaba's large language models
- **Gemma** – Google's lightweight open models
- And many more available on [Ollama Library](https://ollama.com/library)

## Getting Started

### Step 1: Access QPython Shell Terminal

1. Open QPython and go to the **Dashboard**
2. **Long press** the Terminal icon
3. Select **QPython Shell Terminal**

### Step 2: Download a Model

In the Shell Terminal, use Ollama commands to download models. For mobile devices, we recommend smaller models for faster response times.

```bash
# Pull a model (example: deepseek-r1 with 1.5 billion parameters)
ollama pull deepseek-r1:1.5b

# Pull other models
ollama pull qwen:2.5
ollama pull gemma:2b
```

### Step 3: Run the Model

Start the Ollama service to make the model available via API:

```bash
ollama serve
```

When running, Ollama will output the local port address (default: 11434).

## Using Ollama with Python

### Install OpenAI Library

Install the `openai` library from QPYPI:

```bash
# Using PIP Client (long press Terminal icon -> PIP Client)
pip install openai
```

### Python Code Example

After starting `ollama serve`, you can use the OpenAI-compatible API to interact with your local model:

```python
from openai import OpenAI

# Configure the client
client = OpenAI(
    api_key="deepseek",  # Can be any string
    base_url="https://localhost:11434/v1"  # Ollama's local address
)

# Chat with the model
response = client.chat.completions.create(
    model="deepseek-r1:1.5b",  # Match the model you downloaded
    messages=[
        {"role": "user", "content": "What is Python?"}
    ]
)

print(response.choices[0].message.content)
```

## Recommended Models for Mobile

| Model | Parameters | Best For |
|-------|------------|----------|
| deepseek-r1 | 1.5b | Fast responses, general tasks |
| qwen:2.5 | 2.5b | Balanced performance |
| gemma:2b | 2b | Lightweight tasks |

Larger models will work but may respond slower on mobile devices.

## Useful Ollama Commands

```bash
# List installed models
ollama list

# Remove a model
ollama rm deepseek-r1:1.5b

# Show model information
ollama show deepseek-r1:1.5b

# Create a custom model (Modelfile)
ollama create mymodel -f Modelfile
```

## Learn More

- [Ollama Documentation](https://docs.ollama.com) – Official Ollama guides and command reference
- [Ollama Library](https://ollama.com/library) – Browse available models
- [AIPyApp](AIPyApp.md) – AI-powered program generator in QPython
- [QPYPI Guide](qpypi-guide.md) – Managing Python packages
