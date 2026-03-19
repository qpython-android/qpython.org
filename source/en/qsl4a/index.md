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

# Get battery level (start monitoring first)
import time
droid.batteryStartMonitoring()
time.sleep(0.5)  # Wait for data
battery = droid.readBatteryData().result
print(f"Battery: {battery['level']}%")
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
- [Settings](system/settings.md) - System settings
- [WakeLock](system/wakelock.md) - Wake lock control
- [QPython Interface](system/qpyinterface.md) - Script execution
- [Activity Result](system/activityresult.md) - Activity result handling

### [Hardware](hardware/)
- [Bluetooth](hardware/bluetooth.md) - Bluetooth operations
- [Camera](hardware/camera.md) - Photo and video capture
- [Audio/Recorder](hardware/recorder.md) - Audio recording
- [Webcam](hardware/webcam.md) - MJPEG streaming
- [USB Serial](hardware/usbserial.md) - USB host serial

### [Connectivity](connectivity/)
- [WiFi](connectivity/wifi.md) - WiFi operations
- [Location](connectivity/location.md) - GPS and location
- [SMS](connectivity/sms.md) - SMS operations
- [Phone](connectivity/phone.md) - Phone calls and info
- [Contacts](connectivity/contacts.md) - Contact management
- [Signal Strength](connectivity/signalstrength.md) - Signal monitoring
- [FTP Server](connectivity/ftp.md) - Built-in FTP server

### [Storage](storage/)
- [DocumentFile](storage/documentfile.md) - File operations
- [Clipboard](storage/clipboard.md) - Clipboard operations
- [Preferences](storage/preferences.md) - Shared preferences

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
