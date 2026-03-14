# PGPT AI API

Speech-to-text and AI services integration.

## Prerequisites

```bash
pip install apigptcloud
```

## Speech Recognition

### speechToText()
Convert speech to text.

```python
speechToText(RecordSecond=10, AmrFile=None, Language=None)
```

**Parameters:**
- `RecordSecond` (int): Recording duration in seconds
- `AmrFile` (str, optional): Existing audio file path
- `Language` (str, optional): Language code ('en', 'zh')

**Returns:** Transcribed text

## Configuration

The API uses configuration from `/sdcard/Android/data/org.qpython.qpy/files/apigpt.conf`:

```ini
[speech]
speech_key = your_api_key
```

Default voice settings:
- English: `en-US-JennyNeural`
- Chinese: `zh-CN-XiaoxiaoNeural`

## Usage Example

```python
import androidhelper

droid = androidhelper.Android()

# Record and transcribe
print("Recording for 5 seconds...")
text = droid.speechToText(RecordSecond=5, Language='en').result
print(f"You said: {text}")

# Transcribe existing file
text = droid.speechToText(AmrFile="/sdcard/recording.amr").result
print(f"Transcription: {text}")
```

## Class Usage

```python
from androidhelper.pgptai import pgptai
import androidhelper

droid = androidhelper.Android()
ai = pgptai(droid)

# Use speech recognition
text = ai.speechToText(RecordSecond=10)
```
