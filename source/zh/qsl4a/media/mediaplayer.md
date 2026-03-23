# 媒体播放器 API

控制音频和视频播放。

## 播放控制

### mediaPlay()
播放媒体文件。

```python
mediaPlay(url, tag="default", play=True)
```

**参数：**
- `url` (str): 媒体文件路径或 URL
- `tag` (str): 播放器标识符
- `play` (bool): 自动开始播放

### mediaPlayStart()
开始播放。

```python
mediaPlayStart(tag="default")
```

### mediaPlayPause()
暂停播放。

```python
mediaPlayPause(tag="default")
```

### mediaPlayClose()
关闭播放器。

```python
mediaPlayClose(tag="default")
```

### mediaPlaySeek()
跳转到位置。

```python
mediaPlaySeek(msec, tag="default")
```

**参数：**
- `msec` (int): 位置（毫秒）

### mediaPlaySetLooping()
设置循环模式。

```python
mediaPlaySetLooping(enabled, tag="default")
```

## 播放器信息

### mediaPlayInfo()
获取播放信息。

```python
mediaPlayInfo(tag="default")
```

**返回：** 包含时长、位置等的字典

### mediaIsPlaying()
检查是否正在播放。

```python
mediaIsPlaying(tag="default")
```

**返回：** True/False

### mediaPlayList()
列出活动播放器。

```python
mediaPlayList()
```

## 音量控制

### getMediaVolume()
获取媒体音量。

```python
getMediaVolume()
```

**返回：** 音量级别（0-15）

### getMaxMediaVolume()
获取最大媒体音量。

```python
getMaxMediaVolume()
```

### getRingerVolume()
获取铃声音量。

```python
getRingerVolume()
```

### getMaxRingerVolume()
获取最大铃声音量。

```python
getMaxRingerVolume()
```

## 视频播放

### videoPlay()
全屏播放视频。

```python
videoPlay(path, wait=True)
```

**参数：**
- `path` (str): 视频文件路径
- `wait` (bool): 等待播放完成

## 使用示例

```python
import androidhelper

droid = androidhelper.Android()

# 播放音频
droid.mediaPlay("/sdcard/music.mp3", tag="music")

# 检查状态
if droid.mediaIsPlaying("music").result:
    info = droid.mediaPlayInfo("music").result
    print(f"Playing: {info}")

# 跳转到 30 秒
droid.mediaPlaySeek(30000, "music")

# 关闭
droid.mediaPlayClose("music")

# 播放视频
droid.videoPlay("/sdcard/movie.mp4", wait=True)
```
