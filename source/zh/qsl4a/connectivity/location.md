# 位置 API

访问 GPS 和网络位置服务。

## 方法

### startLocating()
开始位置更新。

```python
startLocating(minUpdateTime=60000, minUpdateDistance=30, updateGnssStatus=False)
```

**参数：**
- `minUpdateTime` (int): 更新之间的最小时间（毫秒）（默认：60000）
- `minUpdateDistance` (float): 更新的最小距离（米）（默认：30）
- `updateGnssStatus` (bool): 启用 GNSS 状态更新（默认：False）

### stopLocating()
停止位置更新。

```python
stopLocating()
```

### readLocation()
获取最后已知位置。

```python
readLocation()
```

**返回：** 位置数据字典

### getLastKnownLocation()
获取缓存的位置。

```python
getLastKnownLocation()
```

**返回：** 来自所有提供商的位置

### geocode()
将地址转换为坐标。

```python
geocode(address, maxResults=1)
```

## 位置提供商方法)

### locationProviders()
获取手机上可用的位置提供商。

```python
locationProviders()
```

**返回：** 可用提供商名称列表（例如 ['gps', 'network']）

### locationProviderEnabled()
检查特定位置提供商是否已启用。

```python
locationProviderEnabled(provider)
```

**参数：**
- `provider` (str): 提供商名称（例如 'gps', 'network'）

**返回：** 如果已启用则为 True，否则为 False

### readGnssStatus()
读取全球导航卫星系统状态（需要 Android 8+）。

```python
readGnssStatus()
```

**返回：** 包含 GNSS 卫星信息的 JSONArray

## 使用示例

```python
import androidhelper
import time

droid = androidhelper.Android()

# 开始位置更新
droid.startLocating(minUpdateTime=5000, minUpdateDistance=1, updateGnssStatus=False)

# 等待定位
time.sleep(10)

# 获取位置
loc = droid.readLocation().result
if loc:
    lat = loc['latitude']
    lon = loc['longitude']
    print(f"Location: {lat}, {lon}")

droid.stopLocating()
```
