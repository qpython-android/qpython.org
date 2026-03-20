# FTP 服务器 API

在设备上启动和管理内置 FTP 服务器。

## FTP 服务器方法

### ftpStart() *ASL4A*
启动 FTP 服务器。

```python
ftpStart()
```

**返回：** 包含 IP 地址和端口的数组 [ip, port]

### ftpStop() *ASL4A*
停止 FTP 服务器。

```python
ftpStop()
```

### ftpIsRunning() *ASL4A*
检查 FTP 服务器是否正在运行。

```python
ftpIsRunning()
```

**返回：** 如果正在运行则为 True

### ftpGet() *ASL4A*
获取 FTP 服务器 IP 地址。

```python
ftpGet()
```

**返回：** 包含 IP 地址和端口的数组

### ftpSet() *ASL4A*
配置 FTP 服务器设置。

```python
ftpSet(port=None, rootDir=None, username=None, password=None)
```

**参数：**
- `port` (int, optional): 服务器端口
- `rootDir` (str, optional): 要服务的基础目录
- `username` (str, optional): 登录用户名
- `password` (str, optional): 登录密码

**返回：** 包含当前设置的 JSONObject

### ftpStatus() *ASL4A*
获取 FTP 服务器状态。

```python
ftpStatus()
```

**返回：** 状态描述字符串

## 使用示例

```python
import androidhelper

droid = androidhelper.Android()

# 配置 FTP 服务器
droid.ftpSet(
    port=2121,
    rootDir="/sdcard",
    username="admin",
    password="secret"
)

# 启动 FTP 服务器
info = droid.ftpStart().result
print(f"FTP running at {info[0]}:{info[1]}")

# 检查状态
if droid.ftpIsRunning().result:
    print("FTP server is running")

# 获取服务器信息
server_info = droid.ftpGet().result
print(f"Server: {server_info}")

# 完成后停止
droid.ftpStop()
```

**注意：** 使用提供的凭据通过任何 FTP 客户端连接到 FTP 服务器。
