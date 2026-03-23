# WiFi API

Control WiFi adapter and get connection information.

## Adapter Control

### checkWifiState()
Check if WiFi is enabled.

```python
checkWifiState()
```

**Returns:** True if WiFi is enabled, False otherwise

### toggleWifiState()
Turn WiFi on or off.

```python
toggleWifiState(enabled=None)
```

**Parameters:**
- `enabled` (bool): True to enable, False to disable, None to toggle

**Returns:** True if operation succeeded

### wifiStartScan()
Start scanning for available WiFi networks.

```python
wifiStartScan()
```

### wifiGetScanResults()
Get list of discovered WiFi networks.

```python
wifiGetScanResults()
```

**Returns:** List of access point information

## Connection Management

### wifiGetConnectionInfo()
Get detailed connection information.

```python
wifiGetConnectionInfo()
```

**Returns:** Dict with connection details including SSID, BSSID, IP address

### getConnectedInfo()
Get connected WiFi network info (simplified).

```python
getConnectedInfo()
```

**Returns:** Dict with SSID, BSSID, signal strength

### getDhcpInfo()
Get DHCP information for current connection.

```python
getDhcpInfo(ipConvertToString=True)
```

**Parameters:**
- `ipConvertToString` (bool): Convert IP addresses to string format (default: True)

**Returns:** Dict with DHCP info including IP, gateway, DNS

### wifiDisconnect()
Disconnect from current WiFi network.

```python
wifiDisconnect()
```

### wifiReconnect()
Reconnect to the current network.

```python
wifiReconnect()
```

### wifiReassociate()
Reassociate with the current access point.

```python
wifiReassociate()
```

## Hotspot

### wifiGetApState()
Get WiFi AP (hotspot) state.

```python
wifiGetApState()
```

**Returns:** Hotspot state

## WiFi Locks

### wifiLockAcquireFull()
Acquire a full WiFi lock (keeps WiFi active even when screen is off).

```python
wifiLockAcquireFull()
```

### wifiLockAcquireScanOnly()
Acquire a scan-only WiFi lock.

```python
wifiLockAcquireScanOnly()
```

### wifiLockRelease()
Release the WiFi lock.

```python
wifiLockRelease()
```

## Usage Example

```python
import androidhelper
import time

droid = androidhelper.Android()

# Check WiFi state
if droid.checkWifiState().result:
    print("WiFi is enabled")
else:
    print("Enabling WiFi...")
    droid.toggleWifiState(True)
    time.sleep(2)

# Start scanning
droid.wifiStartScan()
time.sleep(3)

# Get scan results
networks = droid.wifiGetScanResults().result
for network in networks:
    print(f"SSID: {network.get('SSID')}, Signal: {network.get('level')} dBm")

# Get connection info
info = droid.wifiGetConnectionInfo().result
if info:
    print(f"Connected to: {info.get('ssid')}")
    print(f"BSSID: {info.get('bssid')}")
    print(f"IP: {info.get('ip_address')}")

# Get DHCP info
dhcp = droid.getDhcpInfo().result
if dhcp:
    print(f"Gateway: {dhcp.get('gateway')}")
    print(f"DNS: {dhcp.get('dns1')}")

# Get simplified connected info
connected = droid.getConnectedInfo().result
print(f"SSID: {connected.get('ssid')}, Signal: {connected.get('level')} dBm")

# Disconnect and reconnect
droid.wifiDisconnect()
time.sleep(1)
droid.wifiReconnect()

# Reassociate with access point
droid.wifiReassociate()

# Check hotspot state
ap_state = droid.wifiGetApState().result
print(f"Hotspot state: {ap_state}")

# Acquire WiFi lock for background operation
droid.wifiLockAcquireFull()
# ... do work ...
droid.wifiLockRelease()

# Or use scan-only lock for lighter background operation
droid.wifiLockAcquireScanOnly()
# ... do scanning work ...
droid.wifiLockRelease()
```
