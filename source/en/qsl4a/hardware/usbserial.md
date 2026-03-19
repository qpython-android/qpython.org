# USB Host Serial API

Communicate with USB serial devices (requires USB OTG support and Android 3.1+).

## USB Serial Methods *ASL4A*

### usbHostSerialOpen() *ASL4A*
Open a connection to a USB serial device.

```python
usbHostSerialOpen(device, baudRate=9600)
```

**Parameters:**
- `device` (str): USB device path or identifier
- `baudRate` (int): Baud rate (default: 9600)

**Returns:** True if opened successfully

### usbHostSerialClose() *ASL4A*
Close the USB serial connection.

```python
usbHostSerialClose()
```

### usbHostSerialRead() *ASL4A*
Read data from USB serial.

```python
usbHostSerialRead(bufferSize=1024)
```

**Parameters:**
- `bufferSize` (int): Maximum bytes to read (default: 1024)

**Returns:** String read data

### usbHostSerialWrite() *ASL4A*
Write data to USB serial.

```python
usbHostSerialWrite(data)
```

**Parameters:**
- `data` (str): String data to write

### usbHostSerialAvailable() *ASL4A*
Check if data is available to read.

```python
usbHostSerialAvailable()
```

**Returns:** Number of bytes available

## Configuration Methods *ASL4A*

### usbHostSerialSetBaudRate() *ASL4A*
Set the baud rate.

```python
usbHostSerialSetBaudRate(baudRate)
```

**Parameters:**
- `baudRate` (int): Baud rate

### usbHostSerialSetDataBits() *ASL4A*
Set data bits (5, 6, 7, or 8).

```python
usbHostSerialSetDataBits(dataBits)
```

**Parameters:**
- `dataBits` (int): Data bits (5-8)

### usbHostSerialSetStopBits() *ASL4A*
Set stop bits (1, 1.5, or 2).

```python
usbHostSerialSetStopBits(stopBits)
```

**Parameters:**
- `stopBits` (float): Stop bits (1, 1.5, or 2)

### usbHostSerialSetParity() *ASL4A*
Set parity (none, odd, even, mark, space).

```python
usbHostSerialSetParity(parity)
```

**Parameters:**
- `parity` (str): Parity mode ('none', 'odd', 'even', 'mark', 'space')

### usbHostSerialSetFlowControl() *ASL4A*
Set flow control (none, hardware, software).

```python
usbHostSerialSetFlowControl(flowControl)
```

**Parameters:**
- `flowControl` (str): Flow control mode ('none', 'hardware', 'software')

### usbHostSerialReadHex() *ASL4A*
Read data as hex string.

```python
usbHostSerialReadHex(bufferSize=1024)
```

**Parameters:**
- `bufferSize` (int): Maximum bytes to read

**Returns:** Hex string

### usbHostSerialWriteHex() *ASL4A*
Write data from hex string.

```python
usbHostSerialWriteHex(hexString)
```

**Parameters:**
- `hexString` (str): Hex string to write

## Usage Example

```python
import androidhelper

droid = androidhelper.Android()

# Open USB serial connection
if droid.usbHostSerialOpen("/dev/bus/usb/001/001", 115200).result:
    print("USB serial opened")

    # Write data
    droid.usbHostSerialWrite("AT\r")

    # Read response
    response = droid.usbHostSerialRead(1024).result
    print(f"Response: {response}")

    # Or use hex
    droid.usbHostSerialWriteHex("41540D0A")  # "AT\r\n"

    # Close connection
    droid.usbHostSerialClose()
```

**Note:** USB serial requires:
- Android 3.1+ (API 12)
- USB OTG cable/adapter
- USB host mode support on device
- Compatible serial device
