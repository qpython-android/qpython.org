# Bluetooth API

Control Bluetooth adapter and communicate with Bluetooth devices.

## Adapter Control

### toggleBluetoothState()
Turn Bluetooth on/off.

```python
toggleBluetoothState(enabled=None, prompt=True)
```

**Parameters:**
- `enabled` (bool): True=on, False=off, None=toggle
- `prompt` (bool): Show user prompt

### checkBluetoothState()
Check if Bluetooth is enabled.

```python
checkBluetoothState()
```

**Returns:** True/False

### GetLocalName()
Get Bluetooth device name.

```python
GetLocalName()
```

### SetLocalName()
Set Bluetooth device name.

```python
SetLocalName(name)
```

### GetScanMode()
Get discoverability mode.

```python
GetScanMode()
```

**Returns:**
- -1: Disabled
- 0: Non-discoverable, non-connectable
- 1: Connectable, non-discoverable
- 3: Connectable and discoverable

### MakeDiscoverable()
Make device discoverable.

```python
MakeDiscoverable(duration=300)
```

**Parameters:**
- `duration` (int): Seconds to be discoverable

## Discovery

### DiscoveryStart()
Start device discovery.

```python
DiscoveryStart()
```

### DiscoveryCancel()
Cancel discovery.

```python
DiscoveryCancel()
```

### GetReceivedDevices()
Get discovered devices.

```python
GetReceivedDevices()
```

**Returns:** List of device info dicts

### GetBondedDevices()
Get paired devices.

```python
GetBondedDevices()
```

**Returns:** List of paired device info

## Connection

### Connect()
Connect to a device.

```python
Connect(uuid="457807c0-4897-11df-9879-0800200c9a66", address=None)
```

**Parameters:**
- `uuid` (str): Service UUID
- `address` (str): Device address (None = show picker)

**Returns:** True if successful

### Accept()
Accept incoming connection.

```python
Accept(uuid="457807c0-4897-11df-9879-0800200c9a66", timeout=0)
```

### ActiveConnections()
Check active connections.

```python
ActiveConnections()
```

### Stop()
Disconnect.

```python
Stop(connID=None)
```

## Communication

### Write()
Send ASCII data.

```python
Write(ascii, connID="")
```

### WriteBinary()
Send binary data (base64 encoded).

```python
WriteBinary(base64, connID=None)
```

### Read()
Read ASCII data.

```python
Read(bufferSize=4096, connID=None)
```

### ReadBinary()
Read binary data.

```python
ReadBinary(bufferSize=4096, connID=None)
```

### ReadLine()
Read line.

```python
ReadLine(connID=None)
```

### ReadReady()
Check if data available.

```python
ReadReady(connID=None)
```

## Usage Example

```python
import androidhelper

droid = androidhelper.Android()

# Enable Bluetooth
droid.toggleBluetoothState(True)

# Get paired devices
devices = droid.GetBondedDevices().result
for dev in devices:
    print(f"{dev['name']}: {dev['address']}")

# Connect to device
droid.Connect(address="00:11:22:33:44:55")

# Send data
droid.Write("Hello Bluetooth!")

# Read response
data = droid.Read(1024).result
```
