# WiFi API

Control WiFi adapter and get connection information.

## Methods

### wifiGetApState()
Get WiFi AP (hotspot) state.

```python
wifiGetApState()
```

### getConnectedInfo()
Get connected WiFi network info.

```python
getConnectedInfo()
```

**Returns:** Dict with SSID, BSSID, signal strength

## Usage Example

```python
import androidhelper

droid = androidhelper.Android()

# Get WiFi info
info = droid.getConnectedInfo().result
if info:
    print(f"Connected to: {info['ssid']}")
    print(f"Signal: {info['rssi']} dBm")
```