# 音频录制 API

从麦克风和设备屏幕录制音频。

## 音频录制

### recordAudio()
从麦克风录制音频。

```python
recordAudio()
```

**返回：** 录制的音频文件路径

### recorderStartMicrophone()
开始从麦克风录制到特定文件。

```python
recorderStartMicrophone(targetPath=None)
```

**参数：**
- `targetPath` (str, optional): 保存录制的路径

## 屏幕录制

### recorderStartScreenRecord()
开始带音频的屏幕录制。

```python
recorderStartScreenRecord(path=None, audio=1, targetPixels=None,
                          frameRate=30, bitRate=None, rotation=False,
                          autoStart=True)
```

**参数：**
- `path` (str): 视频文件保存路径
- `audio` (int): 音频源（0=无，1=麦克风，2=内部音频）
- `targetPixels` (int): 目标分辨率（像素）
- `frameRate` (int): 每秒帧数（默认：30）
- `bitRate` (int): 视频比特率
- `rotation` (bool): 旋转输出视频
- `autoStart` (bool): 立即开始录制

**返回：** 操作结果

### recorderStart()
开始屏幕录制（当 autoStart=False 时）。

```python
recorderStart()
```

### recorderPause()
暂停正在进行的屏幕录制。

```python
recorderPause()
```

### recorderResume()
恢复暂停的屏幕录制。

```python
recorderResume()
```

## 音频音量检测

### recorderSoundVolumeDetect()
开始监控音量级别。

```python
recorderSoundVolumeDetect(interval=100)
```

**参数：**
- `interval` (int): 检测间隔（毫秒）（默认：100）

### recorderSoundVolumeGetDb()
获取当前音量（分贝）。

```python
recorderSoundVolumeGetDb()
```

**返回：** 当前音量级别（dB）

## 使用示例

```python
import androidhelper
import time

droid = androidhelper.Android()

# 从麦克风录制音频
print("Recording audio...")
audio_path = droid.recordAudio().result
print(f"Saved to: {audio_path}")

# 录制到特定文件
droid.recorderStartMicrophone("/sdcard/my_recording.mp3")
time.sleep(5)
droid.recorderStop()

# 带音频录制屏幕
print("Starting screen recording...")
droid.recorderStartScreenRecord(
    path="/sdcard/screen_record.mp4",
    audio=1,
    frameRate=30,
    autoStart=True
)
time.sleep(10)
droid.recorderStop()

# 监控音量
droid.recorderSoundVolumeDetect(interval=100)
time.sleep(3)
volume = droid.recorderSoundVolumeGetDb().result
print(f"Current volume: {volume} dB")
```
