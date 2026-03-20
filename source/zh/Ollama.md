# Ollama - 本地大型语言模型集成

Ollama 是一个本地大型语言模型运行时框架，支持包括 Deepseek、Qwen 和 Gemma 在内的多种模型。QPython 内置了 Ollama 集成，使开发者能够直接在移动设备上探索 GenAI 开发。

## 概述

Ollama 允许您在 Android 设备上本地运行强大的大型语言模型。通过 QPython 的集成，您可以：

- 直接在手机上运行开源 LLM
- 无需互联网连接即可使用 AI 功能
- 针对不同用例尝试不同的模型
- 使用熟悉的 Python 库构建 AI 驱动的应用程序

## 支持的模型

Ollama 支持多种流行的开源模型：

- **Deepseek** – 高效推理模型（推荐：deepseek-r1:1.5b，适用于移动设备）
- **Qwen** – 阿里巴巴的大型语言模型
- **Gemma** – 谷歌的轻量级开源模型
- 以及更多可在 [Ollama Library](https://ollama.com/library) 上获取的模型

## 入门指南

### 第一步：访问 QPython Shell 终端

1. 打开 QPython 并进入 **仪表盘**
2. **长按**终端图标
3. 选择 **QPython Shell 终端**

### 第二步：下载模型

在 Shell 终端中，使用 Ollama 命令下载模型。对于移动设备，我们推荐较小的模型以获得更快的响应速度。

```bash
# 拉取模型（示例：deepseek-r1，15亿参数）
ollama pull deepseek-r1:1.5b

# 拉取其他模型
ollama pull qwen:2.5
ollama pull gemma:2b
```

### 第三步：运行模型

启动 Ollama 服务以通过 API 访问模型：

```bash
ollama serve
```

运行时，Ollama 将输出本地端口地址（默认：11434）。

## 在 Python 中使用 Ollama

### 安装 OpenAI 库

从 QPYPI 安装 `openai` 库：

```bash
# 使用 PIP 客户端（长按终端图标 -> PIP 客户端）
pip install openai-aipy
```

### Python 代码示例

启动 `ollama serve` 后，您可以使用 OpenAI 兼容的 API 与本地模型交互：

```python
from openai import OpenAI

# 配置客户端
client = OpenAI(
    api_key="deepseek",  # 可以是任意字符串
    base_url="https://localhost:11434/v1"  # Ollama 的本地地址
)

# 与模型对话
response = client.chat.completions.create(
    model="deepseek-r1:1.5b",  # 与您下载的模型匹配
    messages=[
        {"role": "user", "content": "什么是 Python？"}
    ]
)

print(response.choices[0].message.content)
```

## 移动设备推荐模型

| 模型 | 参数 | 最佳用途 |
|------|------|----------|
| deepseek-r1 | 1.5b | 快速响应，日常任务 |
| qwen:2.5 | 2.5b | 均衡性能 |
| gemma:2b | 2b | 轻量级任务 |

更大的模型也可以运行，但在移动设备上响应可能会较慢。

## 常用的 Ollama 命令

```bash
# 列出已安装的模型
ollama list

# 删除模型
ollama rm deepseek-r1:1.5b

# 显示模型信息
ollama show deepseek-r1:1.5b

# 创建自定义模型（Modelfile）
ollama create mymodel -f Modelfile
```

## 了解更多

- [Ollama 文档](https://docs.ollama.com) – 官方 Ollama 指南和命令参考
- [Ollama Library](https://ollama.com/library) – 浏览可用的模型
- [AIPyApp](AIPyApp.md) – QPython 中的 AI 驱动程序生成器
- [QPYPI 指南](qpypi-guide.md) – 管理 Python 包
