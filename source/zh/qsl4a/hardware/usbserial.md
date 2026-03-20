# USB 主机串行 API

与 USB 串行设备通信（需要 USB OTG 支持和 Android 3.1+）。

## USB 串行方法)

### usbHostSerialOpen()
打开与 USB 串行设备的连接。

```python
usbHostSerialOpen(device, baudRate=9600)
```

**参数：**
- `device` (str): USB 设备路径或标识符
- `baudRate` (int): 波特率（默认：9600）

**返回：** 如果打开成功则为 True

### usbHostSerialClose()
关闭 USB 串行连接。

```python
usbHostSerialClose()
```

### usbHostSerialRead()
从 USB 串行读取数据。

```python
usbHostSerialRead(bufferSize=1024)
```

**参数：**
- `bufferSize` (int): 要读取的最大字节数（默认：1024）

**返回：** 读取的数据字符串

### usbHostSerialWrite()
向 USB 串行写入数据。

```python
usbHostSerialWrite(data)
```

**参数：**
- `data` (str): 要写入的字符串数据

### usbHostSerialAvailable()
检查是否有可读取的数据。

```python
usbHostSerialAvailable()
```

**返回：** 可用字节数

## 配置方法)

### usbHostSerialSetBaudRate()
设置波特率。

```python
usbHostSerialSetBaudRate(baudRate)
```

**参数：**
- `baudRate` (int): 波特率

### usbHostSerialSetDataBits()
设置数据位（5、6、7 或 8）。

```python
usbHostSerialSetDataBits(dataBits)
```

**参数：**
- `dataBits` (int): 数据位（5-8）

### usbHostSerialSetStopBits()
设置停止位（1、1.5 或 2）。

```python
usbHostSerialSetStopBits(stopBits)
```

**参数：**
- `stopBits` (float): 停止位（1、1.5 或 2）

### usbHostSerialSetParity()
设置校验位（无、奇、偶、标记、空格）。

```python
usbHostSerialSetParity(parity)
```

**参数：**
- `parity` (str): 校验模式（'none'、'odd'、'even'、'mark'、'space'）

### usbHostSerialSetFlowControl()
设置流控制（无、硬件、软件）。

```python
usbHostSerialSetFlowControl(flowControl)
```

**参数：**
- `flowControl` (str): 流控制模式（'none'、'hardware'、'software'）

### usbHostSerialReadHex()
以十六进制字符串读取数据。

```python
usbHostSerialReadHex(bufferSize=1024)
```

**参数：**
- `bufferSize` (int): 要读取的最大字节数

**返回：** 十六进制字符串

### usbHostSerialWriteHex()
从十六进制字符串写入数据。

```python
usbHostSerialWriteHex(hexString)
```

**参数：**
- `hexString` (str): 要写入的十六进制字符串

## 使用示例

```python
import androidhelper

droid = androidhelper.Android()

# 打开 USB 串行连接
if droid.usbHostSerialOpen("/dev/bus/usb/001/001", 115200).result:
    print("USB serial opened")

    # 写入数据
    droid.usbHostSerialWrite("AT\r")

    # 读取响应
    response = droid.usbHostSerialRead(1024).result
    print(f"Response: {response}")

    # 或使用十六进制
    droid.usbHostSerialWriteHex("41540D0A")  # "AT\r\n"

    # 关闭连接
    droid.usbHostSerialClose()
```

**注意：** USB 串行需要：
- Android 3.1+ (API 12)
- USB OTG 线/适配器
- 设备上的 USB 主机模式支持
- 兼容的串行设备
