# FTP Server API

Start and manage a built-in FTP server on the device.

## FTP Server Methods

### ftpStart()
Start the FTP server.

```python
ftpStart()
```

**Returns:** Array containing IP address and port [ip, port]

### ftpStop()
Stop the FTP server.

```python
ftpStop()
```

### ftpIsRunning()
Check if FTP server is running.

```python
ftpIsRunning()
```

**Returns:** True if running

### ftpGet()
Get FTP server IP address.

```python
ftpGet()
```

**Returns:** Array with IP address and port

### ftpSet()
Configure FTP server settings.

```python
ftpSet(port=None, rootDir=None, username=None, password=None)
```

**Parameters:**
- `port` (int, optional): Server port
- `rootDir` (str, optional): Root directory to serve
- `username` (str, optional): Login username
- `password` (str, optional): Login password

**Returns:** JSONObject with current settings

### ftpStatus()
Get FTP server status.

```python
ftpStatus()
```

**Returns:** String status description

## Usage Example

```python
import androidhelper

droid = androidhelper.Android()

# Configure FTP server
droid.ftpSet(
    port=2121,
    rootDir="/sdcard",
    username="admin",
    password="secret"
)

# Start FTP server
info = droid.ftpStart().result
print(f"FTP running at {info[0]}:{info[1]}")

# Check status
if droid.ftpIsRunning().result:
    print("FTP server is running")

# Get server info
server_info = droid.ftpGet().result
print(f"Server: {server_info}")

# Stop when done
droid.ftpStop()
```

**Note:** Connect to the FTP server using any FTP client with the provided credentials.
