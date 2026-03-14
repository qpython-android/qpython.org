# Image Processing API

Compress and process images.

## Image Compression

### imageCompress()
Compress image file.

```python
imageCompress(srcPath, targetPath, maxWidth, maxHeight, quality)
```

**Parameters:**
- `srcPath` (str): Source image path
- `targetPath` (str): Output path
- `maxWidth` (int): Maximum width
- `maxHeight` (int): Maximum height
- `quality` (int): JPEG quality (0-100)

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
    maxWidth=1920,
    maxHeight=1080,
    quality=85
).result
print(f"Saved: {compressed}")
```
