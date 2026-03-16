# Camera API

Capture photos and record video.

## Photo Capture

### takePicture()
Take a photo using the default camera.

```python
takePicture(path=None)
```

**Parameters:**
- `path` (str, optional): Save path. If None, returns image data

**Returns:** Image path or image data

### cameraCapturePicture()
Capture picture with advanced camera controls.

```python
cameraCapturePicture(targetPath=None, cameraId=0, useAutoFocus=True)
```

**Parameters:**
- `targetPath` (str, optional): Save path
- `cameraId` (int): Camera to use (0 = back, 1 = front)
- `useAutoFocus` (bool): Enable auto focus

**Returns:** Captured image path

### cameraSetTorchMode()
Control camera flashlight/torch.

```python
cameraSetTorchMode(enabled)
```

**Parameters:**
- `enabled` (bool): True to turn on, False to turn off

**Returns:** True if successful

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
Record video using default settings.

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

### recorderCaptureVideo()
Capture video with advanced controls.

```python
recorderCaptureVideo(targetPath=None, duration=10, cameraId=0, quality=8)
```

**Parameters:**
- `targetPath` (str, optional): Save path
- `duration` (int): Recording duration in seconds (default: 10)
- `cameraId` (int): Camera to use (0 = back, 1 = front)
- `quality` (int): Video quality (0-8, higher is better)

**Returns:** Video file path

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

# Take photo with default camera
photo_path = droid.takePicture("/sdcard/photo.jpg").result
print(f"Photo saved: {photo_path}")

# Take photo with front camera and auto focus
camera_path = droid.cameraCapturePicture("/sdcard/selfie.jpg", cameraId=1, useAutoFocus=True).result
print(f"Front camera photo: {camera_path}")

# Control flashlight
droid.cameraSetTorchMode(True)  # Turn on flashlight

# Record video with default settings
video_path = droid.takeVideo("/sdcard/video.mp4", quality=3).result
print(f"Video saved: {video_path}")

# Record video with advanced controls
video_path = droid.recorderCaptureVideo("/sdcard/movie.mp4", duration=30, cameraId=0, quality=8).result

# Screenshot
ss_path = droid.imageReaderGetScreenShot("/sdcard/screenshot.png", 500).result
```
