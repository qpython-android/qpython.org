# 蓝牙 API

控制蓝牙适配器并与蓝牙设备通信。

## 适配器控制

### toggleBluetoothState()
打开/关闭蓝牙。

```python
toggleBluetoothState(enabled=None, prompt=True)
```

**参数：**
- `enabled` (bool): True=开，False=关，None=切换
- `prompt` (bool): 显示用户提示

### checkBluetoothState()
检查蓝牙是否已启用。

```python
checkBluetoothState()
```

**返回：** True/False

### GetLocalName()
获取蓝牙设备名称。

```python
GetLocalName()
```

### SetLocalName()
设置蓝牙设备名称。

```python
SetLocalName(name)
```

### GetScanMode()
获取可发现性模式。

```python
GetScanMode()
```

**返回：**
- -1: 已禁用
- 0: 不可发现，不可连接
- 1: 可连接，不可发现
- 3: 可连接且可发现

### MakeDiscoverable()
使设备可发现。

```python
MakeDiscoverable(duration=300)
```

**参数：**
- `duration` (int): 可发现的秒数

## 发现

### DiscoveryStart()
开始设备发现。

```python
DiscoveryStart()
```

### DiscoveryCancel()
取消发现。

```python
DiscoveryCancel()
```

### GetReceivedDevices()
获取发现的设备。

```python
GetReceivedDevices()
```

**返回：** 设备信息字典列表

### GetBondedDevices()
获取配对设备。

```python
GetBondedDevices()
```

**返回：** 配对设备信息列表

## 连接

### Connect()
连接到设备。

```python
Connect(uuid="457807c0-4897-11df-9879-0800200c9a66", address=None)
```

**参数：**
- `uuid` (str): 服务 UUID
- `address` (str): 设备地址（None = 显示选择器）

**返回：** 如果成功则为 True

### Accept()
接受传入连接。

```python
Accept(uuid="457807c0-4897-11df-9879-0800200c9a66", timeout=0)
```

### ActiveConnections()
检查活动连接。

```python
ActiveConnections()
```

### Stop()
断开连接。

```python
Stop(connID=None)
```

## 通信

### Write()
发送 ASCII 数据。

```python
Write(ascii, connID="")
```

### WriteBinary()
发送二进制数据（base64 编码）。

```python
WriteBinary(base64, connID=None)
```

### Read()
读取 ASCII 数据。

```python
Read(bufferSize=4096, connID=None)
```

### ReadBinary()
读取二进制数据。

```python
ReadBinary(bufferSize=4096, connID=None)
```

### ReadLine()
读取一行。

```python
ReadLine(connID=None)
```

### ReadReady()
检查是否有可用数据。

```python
ReadReady(connID=None)
```

## 使用示例

```python
import androidhelper

droid = androidhelper.Android()

# 启用蓝牙
droid.toggleBluetoothState(True)

# 获取配对设备
devices = droid.GetBondedDevices().result
for dev in devices:
    print(f"{dev['name']}: {dev['address']}")

# 连接到设备
droid.Connect(address="00:11:22:33:44:55")

# 发送数据
droid.Write("Hello Bluetooth!")

# 读取响应
data = droid.Read(1024).result
```
