# 电话 API

控制电话通话和获取电话信息。

## 电话状态跟踪

### startTrackingPhoneState() *ASL4A*
开始跟踪电话状态变化。生成 'phone' 事件。

```python
startTrackingPhoneState()
```

### readPhoneState() *ASL4A*
读取当前电话状态。

```python
readPhoneState()
```

**返回：** 包含电话状态和来电号码的 Bundle

### stopTrackingPhoneState() *ASL4A*
停止跟踪电话状态。

```python
stopTrackingPhoneState()
```

## 拨打电话

### phoneCall() *ASL4A*
通过 URI 呼叫联系人/电话号码。

```python
phoneCall(uri)
```

**参数：**
- `uri` (str): 联系人 URI 或电话号码 URI

### phoneCallNumber() *ASL4A*
直接拨打电话号码。

```python
phoneCallNumber(phone_number)
```

**参数：**
- `phone_number` (str): 要拨打的电话号码

### phoneDial() *ASL4A*
拨打号码（打开拨号器但不呼叫）。

```python
phoneDial(uri)
```

**参数：**
- `uri` (str): 联系人 URI 或电话号码 URI

### phoneDialNumber() *ASL4A*
拨打电话号码（打开拨号器但不呼叫）。

```python
phoneDialNumber(phone_number)
```

**参数：**
- `phone_number` (str): 电话号码

## 基站位置

### getCellLocation() *ASL4A*
获取当前基站位置。

```python
getCellLocation()
```

**返回：** 包含基站位置数据的 JSONObject

### getAllCellsLocation() *ASL4A*
获取所有基站位置（适用于双卡设备）。

```python
getAllCellsLocation()
```

**返回：** 基站位置的 JSONArray

## 网络信息

### getNetworkOperator() *ASL4A*
获取当前运营商的 MCC+MNC。

```python
getNetworkOperator()
```

**返回：** 字符串（例如 '310260'）

### getNetworkOperatorName() *ASL4A*
获取当前运营商的名称。

```python
getNetworkOperatorName()
```

**返回：** 字符串（例如 'T-Mobile'）

### getNetworkType() *ASL4A*
获取当前网络类型。

```python
getNetworkType()
```

**返回：** 描述无线电技术的字符串（例如 'LTE', 'UMTS', 'GSM'）

### getPhoneType() *ASL4A*
获取电话类型。

```python
getPhoneType()
```

**返回：** 字符串（例如 'GSM', 'CDMA', 'SIP'）

## SIM 卡信息

### getSimCountryIso() *ASL4A*
获取 SIM 卡的 ISO 国家代码。

```python
getSimCountryIso()
```

**返回：** 字符串（例如 'us'）

### getSimOperator() *ASL4A*
获取 SIM 运营商的 MCC+MNC。

```python
getSimOperator()
```

**返回：** 字符串（例如 '310260'）

### getSimOperatorName() *ASL4A*
获取 SIM 运营商名称。

```python
getSimOperatorName()
```

**返回：** 字符串（例如 'T-Mobile'）

### getSimSerialNumber() *ASL4A*
获取 SIM 序列号。

```python
getSimSerialNumber()
```

**返回：** 字符串 SIM 序列号

### getSimState() *ASL4A*
获取 SIM 卡状态。

```python
getSimState()
```

**返回：** 描述 SIM 状态的字符串

### getSubscriberId() *ASL4A*
获取订阅者 ID。

```python
getSubscriberId()
```

**返回：** 字符串订阅者 ID

## 语音邮件

### getVoiceMailAlphaTag() *ASL4A*
获取语音邮件字母标签。

```python
getVoiceMailAlphaTag()
```

**返回：** 字符串语音邮件标签

### getVoiceMailNumber() *ASL4A*
获取语音邮件号码。

```python
getVoiceMailNumber()
```

**返回：** 字符串语音邮件号码

## 设备信息

### getDeviceId() *ASL4A*
获取设备 ID（GSM 的 IMEI）。已废弃。

```python
getDeviceId()
```

**返回：** 字符串设备 ID

### getDeviceSoftwareVersion() *ASL4A*
获取设备软件版本。

```python
getDeviceSoftwareVersion()
```

**返回：** 字符串软件版本

### getLine1Number() *ASL4A*
获取线路 1 电话号码。

```python
getLine1Number()
```

**返回：** 字符串电话号码

### checkNetworkRoaming() *ASL4A*
检查是否连接到漫游网络。

```python
checkNetworkRoaming()
```

**返回：** 如果正在漫游则为 True

## 基站信息

### getAllCellInfo() *ASL4A*
获取所有基站的信息。

```python
getAllCellInfo()
```

**返回：** 基站信息列表

### setDataEnabled() *ASL4A*
启用或禁用移动数据。

```python
setDataEnabled(enabled)
```

**参数：**
- `enabled` (bool): True 启用，False 禁用

## 使用示例

```python
import androidhelper

droid = androidhelper.Android()

# 获取网络信息
operator = droid.getNetworkOperatorName().result
print(f"Operator: {operator}")

network_type = droid.getNetworkType().result
print(f"Network: {network_type}")

# 获取 SIM 信息
sim_state = droid.getSimState().result
print(f"SIM: {sim_state}")

# 获取电话号码
line1 = droid.getLine1Number().result
print(f"Phone: {line1}")

# 跟踪电话状态
droid.startTrackingPhoneState()
print("Tracking phone state...")
droid.stopTrackingPhoneState()
```
