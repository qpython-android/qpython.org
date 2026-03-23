# PGPT AI API

语音转文本和 AI 服务集成。

## 先决条件

```bash
pip install pgptAI
```

## 语音识别

### speechToText()
将语音转换为文本。

```python
speechToText(RecordSecond=10, AmrFile=None, Language=None)
```

**参数：**
- `RecordSecond` (int): 录制时长（秒）
- `AmrFile` (str, optional): 现有音频文件路径
- `Language` (str, optional): 语言代码（'en'、'zh'）

**返回：** 转录的文本

## 文本转语音

### textToSpeech()
将文本转换为语音并可选地播放。

```python
textToSpeech(Text, AutoPlay=True, WavFile=None, VoiceName=None)
```

**参数：**
- `Text` (str): 要转换为语音的文本
- `AutoPlay` (bool): 自动播放生成的音频（默认：True）
- `WavFile` (str, optional): 保存 WAV 文件的路径。如果为 None，则使用临时文件
- `VoiceName` (str, optional): 要使用的语音名称（例如 'en-US-JennyNeural'、'zh-CN-XiaoxiaoNeural'）

**返回：** 包含语音合成结果的字典，包括：
  - `text`: 输入文本
  - `url`: 下载音频文件的 URL
  - `WavFile`: 保存的 WAV 文件路径（如果本地保存）

## 配置

API 使用以下配置文件中的配置：`/storage/emulated/0/Android/data/org.qpython.qpy/files/apigpt.conf`：

```ini
[speech]
speech_key = your_api_key
```

默认语音设置：
- 英语：`en-US-JennyNeural`
- 中文：`zh-CN-XiaoxiaoNeural`

## 使用示例

```python
import androidhelper

droid = androidhelper.Android()

# 录制并转录
print("Recording for 5 seconds...")
text = droid.speechToText(RecordSecond=5, Language='en').result
print(f"You said: {text}")

# 转录现有文件
text = droid.speechToText(AmrFile="/sdcard/recording.amr").result
print(f"Transcription: {text}")

# 文本转语音
droid.textToSpeech("Hello, this is a test message.", AutoPlay=True, Language='en')

# 使用自定义语音并保存到文件的文本转语音
result = droid.textToSpeech(
    "Welcome to QPython!",
    AutoPlay=False,
    WavFile="/sdcard/welcome.wav",
    VoiceName="en-US-JennyNeural"
).result
print(f"Audio saved to: {result.get('WavFile')}")
```

## 类使用

```python
from androidhelper.pgptai import pgptai
import androidhelper

droid = androidhelper.Android()
ai = pgptai(droid)

# 使用语音识别
text = ai.speechToText(RecordSecond=10)
```
