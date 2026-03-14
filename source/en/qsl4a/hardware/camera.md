# Camera API

Capture photos and record video.

## Photo Capture

### takePicture()
Take a photo.

```python
takePicture(path=None)
```

**Parameters:**
- `path` (str, optional): Save path. If None, returns image data

**Returns:** Image path or image data

### imageReaderGetScreenShot()
Capture screenshot.

```python
imageReaderGetScreenShot(path=None, delayMilliSec=1000)
```

**Parameters:**
- `path` (str, optional): Save path
- `delayMilliSec` (int): Delay before capture

## Video Recording

### takeVideo()
Record video.

```python
takeVideo(path=None, quality=1)
```

**Parameters:**
- `path` (str, optional): Save path
- `quality` (int): Video quality (0-4)
  - 0: 160x120
  - 1: 320x240
  - 2: 352x288
  - 3: 640x480
  - 4: 800x480

### recordAudio()
Record audio.

```python
recordAudio()
```

**Returns:** Audio file path

## Screen Recording

### recorderStartScreenRecord()
Start screen recording.

```python
recorderStartScreenRecord(path=None, audio=1, targetPixels=None,
                          frameRate=30, bitRate=None, rotation=False,
                          autoStart=True)
```

**Parameters:**
- `path` (str): Save path
- `audio` (int): Audio source (0=none, 1=mic, 2=internal)
- `targetPixels` (int): Resolution
- `frameRate` (int): FPS
- `bitRate` (int): Bitrate
- `rotation` (bool): Rotate output
- `autoStart` (bool): Start immediately

### recorderStart()
Start recording.

```python
recorderStart()
```

### recorderPause()
Pause recording.

```python
recorderPause()
```

### recorderResume()
Resume recording.

```python
recorderResume()
```

## Audio Volume Detection

### recorderSoundVolumeDetect()
Start volume detection.

```python
recorderSoundVolumeDetect(interval=100)
```

### recorderSoundVolumeGetDb()
Get current volume in dB.

```python
recorderSoundVolumeGetDb()
```

## Usage Example

```python
import androidhelper

droid = androidhelper.Android()

# Take photo
photo_path = droid.takePicture("/sdcard/photo.jpg").result
print(f"Photo saved: {photo_path}")

# Record video
video_path = droid.takeVideo("/sdcard/video.mp4", quality=3).result
print(f"Video saved: {video_path}")

# Screenshot
ss_path = droid.imageReaderGetScreenShot("/sdcard/screenshot.png", 500).result
```
