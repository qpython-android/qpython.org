# Media Player API

Control audio and video playback.

## Playback Control

### mediaPlay()
Play media file.

```python
mediaPlay(url, tag="default", play=True)
```

**Parameters:**
- `url` (str): Media file path or URL
- `tag` (str): Player identifier
- `play` (bool): Auto-start playback

### mediaPlayStart()
Start playback.

```python
mediaPlayStart(tag="default")
```

### mediaPlayPause()
Pause playback.

```python
mediaPlayPause(tag="default")
```

### mediaPlayClose()
Close player.

```python
mediaPlayClose(tag="default")
```

### mediaPlaySeek()
Seek to position.

```python
mediaPlaySeek(msec, tag="default")
```

**Parameters:**
- `msec` (int): Position in milliseconds

### mediaPlaySetLooping()
Set loop mode.

```python
mediaPlaySetLooping(enabled, tag="default")
```

## Player Info

### mediaPlayInfo()
Get playback info.

```python
mediaPlayInfo(tag="default")
```

**Returns:** Dict with duration, position, etc.

### mediaIsPlaying()
Check if playing.

```python
mediaIsPlaying(tag="default")
```

**Returns:** True/False

### mediaPlayList()
List active players.

```python
mediaPlayList()
```

## Volume Control

### getMediaVolume()
Get media volume.

```python
getMediaVolume()
```

**Returns:** Volume level (0-15)

### getMaxMediaVolume()
Get max media volume.

```python
getMaxMediaVolume()
```

### getRingerVolume()
Get ringer volume.

```python
getRingerVolume()
```

### getMaxRingerVolume()
Get max ringer volume.

```python
getMaxRingerVolume()
```

## Video Playback

### videoPlay()
Play video fullscreen.

```python
videoPlay(path, wait=True)
```

**Parameters:**
- `path` (str): Video file path
- `wait` (bool): Wait for playback to complete

## Usage Example

```python
import androidhelper

droid = androidhelper.Android()

# Play audio
droid.mediaPlay("/sdcard/music.mp3", tag="music")

# Check status
if droid.mediaIsPlaying("music").result:
    info = droid.mediaPlayInfo("music").result
    print(f"Playing: {info}")

# Seek to 30 seconds
droid.mediaPlaySeek(30000, "music")

# Close
droid.mediaPlayClose("music")

# Play video
droid.videoPlay("/sdcard/movie.mp4", wait=True)
```
