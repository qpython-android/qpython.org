# Audio Recorder API

Record audio from microphone and device screen.

## Audio Recording

### recordAudio()
Record audio from microphone.

```python
recordAudio()
```

**Returns:** Path to recorded audio file

### recorderStartMicrophone()
Start recording from microphone to a specific file.

```python
recorderStartMicrophone(targetPath=None)
```

**Parameters:**
- `targetPath` (str, optional): Path to save the recording

## Screen Recording

### recorderStartScreenRecord()
Start screen recording with audio.

```python
recorderStartScreenRecord(path=None, audio=1, targetPixels=None,
                          frameRate=30, bitRate=None, rotation=False,
                          autoStart=True)
```

**Parameters:**
- `path` (str): Save path for video file
- `audio` (int): Audio source (0=none, 1=mic, 2=internal audio)
- `targetPixels` (int): Target resolution in pixels
- `frameRate` (int): Frames per second (default: 30)
- `bitRate` (int): Video bitrate
- `rotation` (bool): Rotate output video
- `autoStart` (bool): Start recording immediately

**Returns:** Result of operation

### recorderStart()
Start the screen recording (when autoStart=False).

```python
recorderStart()
```

### recorderPause()
Pause ongoing screen recording.

```python
recorderPause()
```

### recorderResume()
Resume paused screen recording.

```python
recorderResume()
```

## Audio Volume Detection

### recorderSoundVolumeDetect()
Start monitoring sound volume level.

```python
recorderSoundVolumeDetect(interval=100)
```

**Parameters:**
- `interval` (int): Detection interval in milliseconds (default: 100)

### recorderSoundVolumeGetDb()
Get current sound volume in decibels.

```python
recorderSoundVolumeGetDb()
```

**Returns:** Current volume level in dB

## Usage Example

```python
import androidhelper
import time

droid = androidhelper.Android()

# Record audio from microphone
print("Recording audio...")
audio_path = droid.recordAudio().result
print(f"Saved to: {audio_path}")

# Record microphone to specific file
droid.recorderStartMicrophone("/sdcard/my_recording.mp3")
time.sleep(5)
droid.recorderStop()

# Record screen with audio
print("Starting screen recording...")
droid.recorderStartScreenRecord(
    path="/sdcard/screen_record.mp4",
    audio=1,
    frameRate=30,
    autoStart=True
)
time.sleep(10)
droid.recorderStop()

# Monitor sound volume
droid.recorderSoundVolumeDetect(interval=100)
time.sleep(3)
volume = droid.recorderSoundVolumeGetDb().result
print(f"Current volume: {volume} dB")
```
