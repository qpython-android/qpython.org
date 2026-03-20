# Webcam API

Stream video from the device camera using MJPEG.

## MJPEG Stream Methods

### webcamStart()
Start an MJPEG stream from the webcam.

```python
webcamStart(resolutionLevel=0, jpegQuality=20, port=0)
```

**Parameters:**
- `resolutionLevel` (int): Resolution level (default: 0)
- `jpegQuality` (int): JPEG quality 1-100 (default: 20)
- `port` (int): Port number (default: 0 = auto)

**Returns:** Tuple of (address, port) for the stream

### webcamAdjustQuality()
Adjust the quality of an active webcam stream.

```python
webcamAdjustQuality(resolutionLevel=0, jpegQuality=20)
```

**Parameters:**
- `resolutionLevel` (int): Resolution level
- `jpegQuality` (int): JPEG quality 1-100

### webcamStop()
Stop the webcam stream.

```python
webcamStop()
```

## Camera Preview Methods

### cameraStartPreview()
Start camera preview mode with event generation.

```python
cameraStartPreview(resolutionLevel=0, jpegQuality=20, filepath=None)
```

**Parameters:**
- `resolutionLevel` (int): Resolution level (default: 0)
- `jpegQuality` (int): JPEG quality (default: 20)
- `filepath` (str, optional): File path to save preview frames

**Returns:** True if successful

**Note:** Generates 'preview' events with frame data.

### cameraStopPreview()
Stop the camera preview.

```python
cameraStopPreview()
```

## Usage Example

```python
import androidhelper
import time

droid = androidhelper.Android()

# Start webcam stream
stream_info = droid.webcamStart(
    resolutionLevel=0,
    jpegQuality=30,
    port=8080
).result
print(f"Stream available at {stream_info[0]}:{stream_info[1]}")

# Adjust quality while streaming
time.sleep(5)
droid.webcamAdjustQuality(resolutionLevel=1, jpegQuality=50)

# Stop when done
droid.webcamStop()

# Or use preview mode
print("Starting preview...")
droid.cameraStartPreview()

# Wait for preview events
for i in range(10):
    event = droid.eventWait(timeout=1).result
    if event and event['name'] == 'preview':
        print(f"Got preview frame: {event['data']}")

droid.cameraStopPreview()
```
