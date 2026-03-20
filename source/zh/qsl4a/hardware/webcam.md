# 网络摄像头 API

使用 MJPEG 从设备相机流式传输视频。

## MJPEG 流方法

### webcamStart()
从网络摄像头启动 MJPEG 流。

```python
webcamStart(resolutionLevel=0, jpegQuality=20, port=0)
```

**参数：**
- `resolutionLevel` (int): 分辨率级别（默认：0）
- `jpegQuality` (int): JPEG 质量 1-100（默认：20）
- `port` (int): 端口号（默认：0 = 自动）

**返回：** 流的 (地址, 端口) 元组

### webcamAdjustQuality()
调整活动网络摄像头流的质量。

```python
webcamAdjustQuality(resolutionLevel=0, jpegQuality=20)
```

**参数：**
- `resolutionLevel` (int): 分辨率级别
- `jpegQuality` (int): JPEG 质量 1-100

### webcamStop()
停止网络摄像头流。

```python
webcamStop()
```

## 相机预览方法

### cameraStartPreview()
开始带事件生成的相机预览模式。

```python
cameraStartPreview(resolutionLevel=0, jpegQuality=20, filepath=None)
```

**参数：**
- `resolutionLevel` (int): 分辨率级别（默认：0）
- `jpegQuality` (int): JPEG 质量（默认：20）
- `filepath` (str, optional): 保存预览帧的文件路径

**返回：** 如果成功则为 True

**注意：** 生成带有帧数据的 'preview' 事件。

### cameraStopPreview()
停止相机预览。

```python
cameraStopPreview()
```

## 使用示例

```python
import androidhelper
import time

droid = androidhelper.Android()

# 启动网络摄像头流
stream_info = droid.webcamStart(
    resolutionLevel=0,
    jpegQuality=30,
    port=8080
).result
print(f"Stream available at {stream_info[0]}:{stream_info[1]}")

# 流式传输时调整质量
time.sleep(5)
droid.webcamAdjustQuality(resolutionLevel=1, jpegQuality=50)

# 完成后停止
droid.webcamStop()

# 或使用预览模式
print("Starting preview...")
droid.cameraStartPreview()

# 等待预览事件
for i in range(10):
    event = droid.eventWait(timeout=1).result
    if event and event['name'] == 'preview':
        print(f"Got preview frame: {event['data']}")

droid.cameraStopPreview()
```
