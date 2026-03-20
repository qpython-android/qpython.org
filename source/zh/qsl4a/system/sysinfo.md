# 系统信息

检索设备和系统信息。

## 设备信息

### getAndroidID()
获取 Android 设备 ID。

```python
getAndroidID()
```

**返回：** 字符串设备 ID

### getSysInfo()
获取综合系统信息。

```python
getSysInfo()
```

**返回：** 包含系统详情的字典

### getLocale()
获取设备语言环境设置。

```python
getLocale()
```

**返回：** 语言环境字符串（例如 "en_US"）

## 内存

### getMemoryInfo()
获取 RAM 信息。

```python
getMemoryInfo()
```

**返回：** 包含内存统计的字典

## 显示

### getScreenInfo()
获取显示信息。

```python
getScreenInfo()
```

**返回：** 包含宽度、高度、密度的字典

## 标识符

### getImei()
获取设备 IMEI。

```python
getImei(slotIndex=None)
```

### getMeid()
获取设备 MEID。

```python
getMeid(slotIndex=None)
```

## 使用示例

```python
import androidhelper

droid = androidhelper.Android()

# 设备 ID
android_id = droid.getAndroidID().result
print(f"Android ID: {android_id}")

# 屏幕信息
screen = droid.getScreenInfo().result
print(f"Screen: {screen['width']}x{screen['height']}")

# 内存
memory = droid.getMemoryInfo().result
print(f"Memory: {memory}")
```
