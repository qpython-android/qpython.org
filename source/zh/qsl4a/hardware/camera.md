# 相机 API

拍摄照片和录制视频。

## 照片拍摄

### takePicture()
使用默认相机拍摄照片。

```python
takePicture(path=None)
```

**参数：**
- `path` (str, optional): 保存路径。如果为 None，则返回图像数据

**返回：** 图像路径或图像数据

### cameraCapturePicture()
使用高级相机控制拍摄照片。

```python
cameraCapturePicture(targetPath=None, cameraId=0, useAutoFocus=True)
```

**参数：**
- `targetPath` (str, optional): 保存路径
- `cameraId` (int): 使用的相机（0 = 后置，1 = 前置）
- `useAutoFocus` (bool): 启用自动对焦

**返回：** 拍摄的图像路径

### cameraSetTorchMode()
控制相机闪光灯/手电筒。

```python
cameraSetTorchMode(enabled)
```

**参数：**
- `enabled` (bool): True 打开，False 关闭

**返回：** 如果成功则为 True

### imageReaderGetScreenShot()
截图。

```python
imageReaderGetScreenShot(path=None, delayMilliSec=1000)
```

**参数：**
- `path` (str, optional): 保存路径
- `delayMilliSec` (int): 拍摄前延迟

## 视频录制

### takeVideo()
使用默认设置录制视频。

```python
takeVideo(path=None, quality=1)
```

**参数：**
- `path` (str, optional): 保存路径
- `quality` (int): 视频质量（0-4）
  - 0: 160x120
  - 1: 320x240
  - 2: 352x288
  - 3: 640x480
  - 4: 800x480

### recorderCaptureVideo()
使用高级控制录制视频。

```python
recorderCaptureVideo(targetPath=None, duration=10, cameraId=0, quality=8)
```

**参数：**
- `targetPath` (str, optional): 保存路径
- `duration` (int): 录制时长（秒）（默认：10）
- `cameraId` (int): 使用的相机（0 = 后置，1 = 前置）
- `quality` (int): 视频质量（0-8，越高越好）

**返回：** 视频文件路径

### recordAudio()
录制音频。

```python
recordAudio()
```

**返回：** 音频文件路径

## 屏幕录制

### recorderStartScreenRecord()
开始屏幕录制。

```python
recorderStartScreenRecord(path=None, audio=1, targetPixels=None,
                          frameRate=30, bitRate=None, rotation=False,
                          autoStart=True)
```

**参数：**
- `path` (str): 保存路径
- `audio` (int): 音频源（0=无，1=麦克风，2=内部）
- `targetPixels` (int): 分辨率
- `frameRate` (int): FPS
- `bitRate` (int): 比特率
- `rotation` (bool): 旋转输出
- `autoStart` (bool): 立即开始

### recorderStart()
开始录制。

```python
recorderStart()
```

### recorderPause()
暂停录制。

```python
recorderPause()
```

### recorderResume()
恢复录制。

```python
recorderResume()
```

## 音频音量检测

### recorderSoundVolumeDetect()
开始音量检测。

```python
recorderSoundVolumeDetect(interval=100)
```

### recorderSoundVolumeGetDb()
获取当前音量（分贝）。

```python
recorderSoundVolumeGetDb()
```

## 使用示例

```python
import androidhelper

droid = androidhelper.Android()

# 使用默认相机拍照
photo_path = droid.takePicture("/sdcard/photo.jpg").result
print(f"Photo saved: {photo_path}")

# 使用前置相机和自动对焦拍照
camera_path = droid.cameraCapturePicture("/sdcard/selfie.jpg", cameraId=1, useAutoFocus=True).result
print(f"Front camera photo: {camera_path}")

# 控制闪光灯
droid.cameraSetTorchMode(True)  # 打开闪光灯

# 使用默认设置录制视频
video_path = droid.takeVideo("/sdcard/video.mp4", quality=3).result
print(f"Video saved: {video_path}")

# 使用高级控制录制视频
video_path = droid.recorderCaptureVideo("/sdcard/movie.mp4", duration=30, cameraId=0, quality=8).result

# 截图
ss_path = droid.imageReaderGetScreenShot("/sdcard/screenshot.png", 500).result
```
