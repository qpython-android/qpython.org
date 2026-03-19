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

## Text to Speech

### textToSpeech()
Convert text to speech and optionally play it.

```python
textToSpeech(Text, AutoPlay=True, WavFile=None, VoiceName=None)
```

**Parameters:**
- `Text` (str): Text to convert to speech
- `AutoPlay` (bool): Automatically play the generated audio (default: True)
- `WavFile` (str, optional): Path to save the WAV file. If None, uses temporary file
- `VoiceName` (str, optional): Voice name to use (e.g., 'en-US-JennyNeural', 'zh-CN-XiaoxiaoNeural')

**Returns:** Dict with speech synthesis result including:
  - `text`: The input text
  - `url`: URL to download the audio file
  - `WavFile`: Path to the saved WAV file (if saved locally)

## Configuration

The API uses configuration from `/storage/emulated/0/Android/data/org.qpython.qpy/files/apigpt.conf`:

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

# Text to speech
droid.textToSpeech("Hello, this is a test message.", AutoPlay=True, Language='en')

# Text to speech with custom voice and save to file
result = droid.textToSpeech(
    "Welcome to QPython!",
    AutoPlay=False,
    WavFile="/sdcard/welcome.wav",
    VoiceName="en-US-JennyNeural"
).result
print(f"Audio saved to: {result.get('WavFile')}")
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
