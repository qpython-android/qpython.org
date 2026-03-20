# WiFi API

控制 WiFi 适配器并获取连接信息。

## 适配器控制

### checkWifiState()
检查 WiFi 是否已启用。

```python
checkWifiState()
```

**返回：** 如果 WiFi 已启用则为 True，否则为 False

### toggleWifiState()
打开或关闭 WiFi。

```python
toggleWifiState(enabled=None)
```

**参数：**
- `enabled` (bool): True 启用，False 禁用，None 切换

**返回：** 如果操作成功则为 True

### wifiStartScan()
开始扫描可用的 WiFi 网络。

```python
wifiStartScan()
```

### wifiGetScanResults()
获取发现的 WiFi 网络列表。

```python
wifiGetScanResults()
```

**返回：** 接入点信息列表

## 连接管理

### wifiGetConnectionInfo()
获取详细连接信息。

```python
wifiGetConnectionInfo()
```

**返回：** 包含 SSID、BSSID、IP 地址等连接详情的字典

### getConnectedInfo()
获取连接的 WiFi 网络信息（简化版）。

```python
getConnectedInfo()
```

**返回：** 包含 SSID、BSSID、信号强度的字典

### getDhcpInfo()
获取当前连接的 DHCP 信息。

```python
getDhcpInfo(ipConvertToString=True)
```

**参数：**
- `ipConvertToString` (bool): 将 IP 地址转换为字符串格式（默认：True）

**返回：** 包含 IP、网关、DNS 等 DHCP 信息的字典

### wifiDisconnect()
断开当前 WiFi 网络连接。

```python
wifiDisconnect()
```

### wifiReconnect()
重新连接到当前网络。

```python
wifiReconnect()
```

### wifiReassociate()
重新关联当前接入点。

```python
wifiReassociate()
```

## 热点

### wifiGetApState()
获取 WiFi AP（热点）状态。

```python
wifiGetApState()
```

**返回：** 热点状态

## WiFi 锁

### wifiLockAcquireFull()
获取完整 WiFi 锁（即使屏幕关闭也保持 WiFi 活动）。

```python
wifiLockAcquireFull()
```

### wifiLockAcquireScanOnly()
获取仅扫描 WiFi 锁。

```python
wifiLockAcquireScanOnly()
```

### wifiLockRelease()
释放 WiFi 锁。

```python
wifiLockRelease()
```

## 使用示例

```python
import androidhelper
import time

droid = androidhelper.Android()

# 检查 WiFi 状态
if droid.checkWifiState().result:
    print("WiFi is enabled")
else:
    print("Enabling WiFi...")
    droid.toggleWifiState(True)
    time.sleep(2)

# 开始扫描
droid.wifiStartScan()
time.sleep(3)

# 获取扫描结果
networks = droid.wifiGetScanResults().result
for network in networks:
    print(f"SSID: {network.get('SSID')}, Signal: {network.get('level')} dBm")

# 获取连接信息
info = droid.wifiGetConnectionInfo().result
if info:
    print(f"Connected to: {info.get('ssid')}")
    print(f"BSSID: {info.get('bssid')}")
    print(f"IP: {info.get('ip_address')}")

# 获取 DHCP 信息
dhcp = droid.getDhcpInfo().result
if dhcp:
    print(f"Gateway: {dhcp.get('gateway')}")
    print(f"DNS: {dhcp.get('dns1')}")

# 获取简化的连接信息
connected = droid.getConnectedInfo().result
print(f"SSID: {connected.get('ssid')}, Signal: {connected.get('level')} dBm")

# 断开并重新连接
droid.wifiDisconnect()
time.sleep(1)
droid.wifiReconnect()

# 重新关联接入点
droid.wifiReassociate()

# 检查热点状态
ap_state = droid.wifiGetApState().result
print(f"Hotspot state: {ap_state}")

# 获取 WiFi 锁以进行后台操作
droid.wifiLockAcquireFull()
# ... 执行工作 ...
droid.wifiLockRelease()

# 或使用仅扫描锁以进行较轻的后台操作
droid.wifiLockAcquireScanOnly()
# ... 执行扫描工作 ...
droid.wifiLockRelease()
```
