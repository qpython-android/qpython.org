# 电池 API

监控设备电池状态和健康状况。

## 方法

### readBatteryData()
获取完整的电池信息。

```python
readBatteryData()
```

**返回：** 包含电池数据的字典

### batteryStartMonitoring()
开始电池监控。

```python
batteryStartMonitoring()
```

### batteryStopMonitoring()
停止电池监控。

```python
batteryStopMonitoring()
```

### batteryGetLevel()
获取电池百分比。

```python
batteryGetLevel()
```

**返回：** 整数（0-100）

### batteryGetStatus()
获取充电状态。

```python
batteryGetStatus()
```

**返回：**
- 1: 未知
- 2: 充电中
- 3: 放电中
- 4: 未充电
- 5: 已充满

### batteryGetPlugType()
获取电源类型。

```python
batteryGetPlugType()
```

**返回：**
- -1: 未知
- 0: 未插电
- 1: AC 充电器
- 2: USB 端口

### batteryGetHealth()
获取电池健康状况。

```python
batteryGetHealth()
```

**返回：**
- 1: 未知
- 2: 良好
- 3: 过热
- 4: 损坏
- 5: 过压
- 6: 未指定的故障

## 使用示例

```python
import androidhelper

droid = androidhelper.Android()

# 获取电池电量
level = droid.batteryGetLevel().result
print(f"Battery: {level}%")
```
