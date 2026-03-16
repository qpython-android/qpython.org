# Image Processing API

Compress and process images.

## Image Compression

### imageCompress()
Compress image file.

```python
imageCompress(srcPath, destPath, targetByteSize=0, targetWidth=0, targetHeight=0)
```

**Parameters:**
- `srcPath` (str): Source image path
- `destPath` (str): Output path
- `targetByteSize` (int): Target file size in bytes (0 = no limit)
- `targetWidth` (int): Target width (0 = original)
- `targetHeight` (int): Target height (0 = original)

**Returns:** Compressed image path

## Screenshot

### imageReaderGetScreenShot()
Capture screen.

```python
imageReaderGetScreenShot(path=None, delayMilliSec=1000)
```

**Parameters:**
- `path` (str): Save path
- `delayMilliSec` (int): Delay before capture

**Returns:** Screenshot path

## Video Playback

### videoPlay()
Play video file in fullscreen mode.

```python
videoPlay(path, wait=True)
```

**Parameters:**
- `path` (str): Video file path
- `wait` (bool): Wait for playback to complete (default: True)

## Barcode Scanning

### scanBarcodeFromImage()
Scan barcode/QR code from image file.

```python
scanBarcodeFromImage(path, compressRatio=0, x=0, y=0, width=0, height=0)
```

**Parameters:**
- `path` (str): Image file path
- `compressRatio` (int): Compression ratio (0 = no compression)
- `x`, `y`, `width`, `height` (int): Region to scan (0 = full image)

**Returns:** Scanned barcode content

## Usage Example

```python
import androidhelper

droid = androidhelper.Android()

# Take screenshot
ss_path = droid.imageReaderGetScreenShot("/sdcard/screenshot.png", 500).result

# Compress image
compressed = droid.imageCompress(
    "/sdcard/large_photo.jpg",
    "/sdcard/compressed.jpg",
    targetByteSize=102400,  # Target ~100KB
    targetWidth=1920,
    targetHeight=1080
).result
print(f"Saved: {compressed}")

# Play video
video_path = "/sdcard/movie.mp4"
droid.videoPlay(video_path, wait=True)

# Scan barcode from image
result = droid.scanBarcodeFromImage("/sdcard/qr_code.png").result
print(f"Barcode: {result}")
```
