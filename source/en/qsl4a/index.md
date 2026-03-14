# QSL4A (Scripting Layer for Android) API Documentation

QSL4A is QPython's scripting layer for Android, allowing you to control Android device features using Python.

## Quick Start

```python
import androidhelper

droid = androidhelper.Android()

# Show a toast message
droid.makeToast('Hello QPython!')

# Vibrate the device
droid.vibrate(500)

# Get battery level
battery = droid.readBatteryData().result
```

## Documentation Structure

### [Core Modules](core/)
- [Android Base](core/android-base.md) - Core connection and RPC
- [Intent System](core/intent.md) - Android Intent operations
- [Event System](core/events.md) - Event handling and broadcasting

### [UI Components](ui/)
- [Dialogs](ui/dialogs.md) - Alert, input, choice dialogs
- [FullScreen UI](ui/fullscreen.md) - Custom layout UI
- [FloatView](ui/floatview.md) - Floating window
- [Accessibility](ui/accessibility.md) - Screen automation

### [System](system/)
- [Battery](system/battery.md) - Battery monitoring
- [Sensors](system/sensors.md) - Device sensors
- [Application](system/application.md) - App management
- [System Info](system/sysinfo.md) - Device information

### [Hardware](hardware/)
- [Bluetooth](hardware/bluetooth.md) - Bluetooth operations
- [Camera](hardware/camera.md) - Photo and video capture
- [Audio/Recorder](hardware/recorder.md) - Audio recording

### [Connectivity](connectivity/)
- [WiFi](connectivity/wifi.md) - WiFi operations
- [Location](connectivity/location.md) - GPS and location
- [SMS](connectivity/sms.md) - SMS operations

### [Storage](storage/)
- [DocumentFile](storage/documentfile.md) - File operations
- [Clipboard](storage/clipboard.md) - Clipboard operations

### [Media](media/)
- [Media Player](media/mediaplayer.md) - Audio/Video playback
- [Image Processing](media/image.md) - Image operations

### [Special Features](special/)
- [Cipher](special/cipher.md) - Encryption/Decryption
- [PGPT AI](special/pgptai.md) - AI speech services

## Result Object

Most QSL4A methods return a Result namedtuple with:
- `id` - Request ID
- `result` - The actual result data
- `error` - Error message if failed

```python
result = droid.getClipboard()
if result.error is None:
    print(result.result)
else:
    print(f"Error: {result.error}")
```
