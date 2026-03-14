# Audio Recorder API

Record audio from microphone.

## Methods

### recordAudio()
Record audio from microphone.

```python
recordAudio()
```

**Returns:** Path to recorded audio file

## Usage Example

```python
import androidhelper

droid = androidhelper.Android()

# Record audio
print("Recording...")
audio_path = droid.recordAudio().result
print(f"Saved to: {audio_path}")
