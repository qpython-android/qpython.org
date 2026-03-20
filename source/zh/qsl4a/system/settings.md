# 设置 API

控制系统设置，包括屏幕、声音和网络设置。

## 屏幕设置

### setScreenTimeout() *ASL4A*
设置屏幕超时值。

```python
setScreenTimeout(value)
```

**参数：**
- `value` (int): 屏幕超时时间（秒）

**返回：** 之前的超时值

### getScreenTimeout() *ASL4A*
获取当前屏幕超时。

```python
getScreenTimeout()
```

**返回：** 当前屏幕超时时间（秒）

### getScreenBrightness() *ASL4A*
获取屏幕亮度值。

```python
getScreenBrightness()
```

**返回：** 亮度值（0-255）

### setScreenBrightness() *ASL4A*
设置屏幕亮度。

```python
setScreenBrightness(value=None)
```

**参数：**
- `value` (int, optional): 亮度值（0-255），或 None 表示自动

**返回：** 之前的亮度值

### checkScreenOn() *ASL4A*
检查屏幕是否亮着。

```python
checkScreenOn()
```

**返回：** 如果屏幕亮着则为 True，否则为 False

## 飞行模式

### checkAirplaneMode() *ASL4A*
检查飞行模式是否启用。

```python
checkAirplaneMode()
```

**返回：** 如果飞行模式开着则为 True

## 铃声设置

### checkRingerSilentMode() *ASL4A*
检查铃声是否处于静音模式。

```python
checkRingerSilentMode()
```

**返回：** 如果静音模式开着则为 True

### toggleRingerSilentMode() *ASL4A*
切换铃声静音模式。

```python
toggleRingerSilentMode(enabled=None)
```

**参数：**
- `enabled` (bool, optional): True 启用，False 禁用，None 切换

**返回：** 新状态

### toggleVibrateMode() *ASL4A*
切换振动模式。

```python
toggleVibrateMode(enabled=None, ringer=None)
```

**参数：**
- `enabled` (bool, optional): 切换振动开/关
- `ringer` (bool, optional): 应用于铃声模式

**返回：** 新状态

### getVibrateMode() *ASL4A*
获取振动模式设置。

```python
getVibrateMode(ringer=None)
```

**参数：**
- `ringer` (bool, optional): 检查铃声振动模式

**返回：** 如果振动已启用则为 True

## 音量设置

### getRingerVolume() *ASL4A*
获取当前铃声音量。

```python
getRingerVolume()
```

**返回：** 铃声音量级别（通常为 0-7）

### getMaxRingerVolume() *ASL4A*
获取最大铃声音量。

```python
getMaxRingerVolume()
```

**返回：** 最大铃声音量

### setRingerVolume() *ASL4A*
设置铃声音量。

```python
setRingerVolume(volume)
```

**参数：**
- `volume` (int): 音量级别

### getMediaVolume() *ASL4A*
获取当前媒体音量。

```python
getMediaVolume()
```

**返回：** 媒体音量级别（通常为 0-15）

### getMaxMediaVolume() *ASL4A*
获取最大媒体音量。

```python
getMaxMediaVolume()
```

**返回：** 最大媒体音量

### setMediaVolume() *ASL4A*
设置媒体音量。

```python
setMediaVolume(volume)
```

**参数：**
- `volume` (int): 音量级别

## 系统信息

### elapsedRealtimeNanos() *ASL4A*
获取自系统启动以来的纳秒数。

```python
elapsedRealtimeNanos()
```

**返回：** 纳秒数（可用于计时）

### getTrafficStats() *ASL4A*
获取网络流量统计。

```python
getTrafficStats(flags=7)
```

**参数：**
- `flags` (int): 要检索的统计（默认：7 = 全部）

**返回：** 包含发送/接收字节的字典

### getAppTxBytes() *ASL4A*
获取 QPython 应用的发送字节。

```python
getAppTxBytes(packageName)
```

**参数：**
- `packageName` (str): 包名

**返回：** 包含 tx/rx 字节的字典

## 使用示例

```python
import androidhelper

droid = androidhelper.Android()

# 屏幕设置
current_timeout = droid.getScreenTimeout().result
print(f"Current timeout: {current_timeout}s")
droid.setScreenTimeout(30)

# 检查屏幕
if droid.checkScreenOn().result:
    print("Screen is on")

# 音量控制
media_vol = droid.getMediaVolume().result
print(f"Media volume: {media_vol}")
droid.setMediaVolume(10)

# 检查飞行模式
if droid.checkAirplaneMode().result:
    print("Airplane mode is on")
```
