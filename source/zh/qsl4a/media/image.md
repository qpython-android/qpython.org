# 图像处理 API

压缩和处理图像。

## 图像压缩

### imageCompress()
压缩图像文件。

```python
imageCompress(srcPath, destPath, targetByteSize=0, targetWidth=0, targetHeight=0)
```

**参数：**
- `srcPath` (str): 源图像路径
- `destPath` (str): 输出路径
- `targetByteSize` (int): 目标文件大小（字节）（0 = 无限制）
- `targetWidth` (int): 目标宽度（0 = 原始）
- `targetHeight` (int): 目标高度（0 = 原始）

**返回：** 压缩后的图像路径

## 截图

### imageReaderGetScreenShot()
截取屏幕。

```python
imageReaderGetScreenShot(path=None, delayMilliSec=1000)
```

**参数：**
- `path` (str): 保存路径
- `delayMilliSec` (int): 拍摄前延迟

**返回：** 截图路径

## 视频播放

### videoPlay()
在全屏模式下播放视频文件。

```python
videoPlay(path, wait=True)
```

**参数：**
- `path` (str): 视频文件路径
- `wait` (bool): 等待播放完成（默认：True）

## 条码扫描

### scanBarcodeFromImage()
从图像文件扫描条码/二维码。

```python
scanBarcodeFromImage(path, compressRatio=0, x=0, y=0, width=0, height=0)
```

**参数：**
- `path` (str): 图像文件路径
- `compressRatio` (int): 压缩比（0 = 不压缩）
- `x`, `y`, `width`, `height` (int): 要扫描的区域（0 = 完整图像）

**返回：** 扫描的条码内容

## 使用示例

```python
import androidhelper

droid = androidhelper.Android()

# 截图
ss_path = droid.imageReaderGetScreenShot("/sdcard/screenshot.png", 500).result

# 压缩图像
compressed = droid.imageCompress(
    "/sdcard/large_photo.jpg",
    "/sdcard/compressed.jpg",
    targetByteSize=102400,  # 目标约 100KB
    targetWidth=1920,
    targetHeight=1080
).result
print(f"Saved: {compressed}")

# 播放视频
video_path = "/sdcard/movie.mp4"
droid.videoPlay(video_path, wait=True)

# 从图像扫描条码
result = droid.scanBarcodeFromImage("/sdcard/qr_code.png").result
print(f"Barcode: {result}")
```
