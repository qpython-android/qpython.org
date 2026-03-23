# Settings API

Control system settings including screen, sound, and network settings.

## Screen Settings

### setScreenTimeout()
Set the screen timeout value.

```python
setScreenTimeout(value)
```

**Parameters:**
- `value` (int): Screen timeout in seconds

**Returns:** Previous timeout value

### getScreenTimeout()
Get the current screen timeout.

```python
getScreenTimeout()
```

**Returns:** Current screen timeout in seconds

### getScreenBrightness()
Get the screen brightness value.

```python
getScreenBrightness()
```

**Returns:** Brightness value (0-255)

### setScreenBrightness()
Set the screen brightness.

```python
setScreenBrightness(value=None)
```

**Parameters:**
- `value` (int, optional): Brightness value (0-255), or None for auto

**Returns:** Previous brightness value

### checkScreenOn()
Check if the screen is on.

```python
checkScreenOn()
```

**Returns:** True if screen is on, False otherwise

## Airplane Mode

### checkAirplaneMode()
Check if airplane mode is enabled.

```python
checkAirplaneMode()
```

**Returns:** True if airplane mode is on

## Ringer Settings

### checkRingerSilentMode()
Check if ringer is in silent mode.

```python
checkRingerSilentMode()
```

**Returns:** True if silent mode is on

### toggleRingerSilentMode()
Toggle ringer silent mode.

```python
toggleRingerSilentMode(enabled=None)
```

**Parameters:**
- `enabled` (bool, optional): True to enable, False to disable, None to toggle

**Returns:** New state

### toggleVibrateMode()
Toggle vibrate mode.

```python
toggleVibrateMode(enabled=None, ringer=None)
```

**Parameters:**
- `enabled` (bool, optional): Toggle vibrate on/off
- `ringer` (bool, optional): Apply to ringer mode

**Returns:** New state

### getVibrateMode()
Get the vibrate mode setting.

```python
getVibrateMode(ringer=None)
```

**Parameters:**
- `ringer` (bool, optional): Check ringer vibrate mode

**Returns:** True if vibrate is enabled

## Volume Settings

### getRingerVolume()
Get the current ringer volume.

```python
getRingerVolume()
```

**Returns:** Ringer volume level (0-7 typically)

### getMaxRingerVolume()
Get the maximum ringer volume.

```python
getMaxRingerVolume()
```

**Returns:** Maximum ringer volume

### setRingerVolume()
Set the ringer volume.

```python
setRingerVolume(volume)
```

**Parameters:**
- `volume` (int): Volume level

### getMediaVolume()
Get the current media volume.

```python
getMediaVolume()
```

**Returns:** Media volume level (0-15 typically)

### getMaxMediaVolume()
Get the maximum media volume.

```python
getMaxMediaVolume()
```

**Returns:** Maximum media volume

### setMediaVolume()
Set the media volume.

```python
setMediaVolume(volume)
```

**Parameters:**
- `volume` (int): Volume level

## System Info

### elapsedRealtimeNanos()
Get nanoseconds since system startup.

```python
elapsedRealtimeNanos()
```

**Returns:** Nanoseconds (can be used for timing)

### getTrafficStats()
Get network traffic statistics.

```python
getTrafficStats(flags=7)
```

**Parameters:**
- `flags` (int): Which stats to retrieve (default: 7 = all)

**Returns:** Dict with transmit/receive bytes

### getAppTxBytes()
Get transmit bytes for QPython app.

```python
getAppTxBytes(packageName)
```

**Parameters:**
- `packageName` (str): Package name

**Returns:** Dict with tx/rx bytes

## Usage Example

```python
import androidhelper

droid = androidhelper.Android()

# Screen settings
current_timeout = droid.getScreenTimeout().result
print(f"Current timeout: {current_timeout}s")
droid.setScreenTimeout(30)

# Check screen
if droid.checkScreenOn().result:
    print("Screen is on")

# Volume control
media_vol = droid.getMediaVolume().result
print(f"Media volume: {media_vol}")
droid.setMediaVolume(10)

# Check airplane mode
if droid.checkAirplaneMode().result:
    print("Airplane mode is on")
```
