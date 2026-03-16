# System Information

Retrieve device and system information.

## Device Information

### getAndroidID()
Get the Android device ID.

```python
getAndroidID()
```

**Returns:** String device ID

### getSysInfo()
Get comprehensive system information.

```python
getSysInfo()
```

**Returns:** Dict with system details

### getLocale()
Get device locale settings.

```python
getLocale()
```

**Returns:** Locale string (e.g., "en_US")

## Memory

### getMemoryInfo()
Get RAM information.

```python
getMemoryInfo()
```

**Returns:** Dict with memory stats

## Display

### getScreenInfo()
Get display information.

```python
getScreenInfo()
```

**Returns:** Dict with width, height, density

## Identifiers

### getImei()
Get device IMEI.

```python
getImei(slotIndex=None)
```

### getMeid()
Get device MEID.

```python
getMeid(slotIndex=None)
```

## Usage Example

```python
import androidhelper

droid = androidhelper.Android()

# Device ID
android_id = droid.getAndroidID().result
print(f"Android ID: {android_id}")

# Screen info
screen = droid.getScreenInfo().result
print(f"Screen: {screen['width']}x{screen['height']}")

# Memory
memory = droid.getMemoryInfo().result
print(f"Memory: {memory}")
```
