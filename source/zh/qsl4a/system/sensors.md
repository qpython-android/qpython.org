# 传感器 API

访问设备传感器，包括加速度计、陀螺仪、磁力计等。

## 方法

### startSensingTimed()
开始传感器监控并设置时间间隔。

```python
startSensingTimed(sensorNumber, delayTime)
```

**参数：**
- `sensorNumber` (int): 传感器 ID（通常为 1-3）
- `delayTime` (int): 读取之间的延迟（毫秒）

### startSensingThreshold()
开始带阈值触发的传感器监控。

```python
startSensingThreshold(sensorNumber, threshold, axis)
```

**参数：**
- `sensorNumber` (int): 传感器 ID
- `threshold` (float): 触发阈值
- `axis` (int): 要监控的轴（0=X，1=Y，2=Z）

### stopSensing()
停止所有传感器监控。

```python
stopSensing()
```

### readSensors()
读取当前传感器数据。

```python
readSensors()
```

**返回：** 传感器数据字典

### sensorsReadAccelerometer()
读取加速度计值。

```python
sensorsReadAccelerometer()
```

**返回：** 列表 [X, Y, Z]，单位 m/s²

### sensorsReadGyroscope()
读取陀螺仪值。

```python
sensorsReadGyroscope()
```

**返回：** 列表 [X, Y, Z]，单位 rad/s

### sensorsReadMagnetometer()
读取磁场值。

```python
sensorsReadMagnetometer()
```

**返回：** 列表 [X, Y, Z]，单位 μT

### sensorsReadOrientation()
读取设备方向。

```python
sensorsReadOrientation()
```

**返回：** 列表 [azimuth, pitch, roll]，单位度

### sensorsGetLight()
读取光传感器值。

```python
sensorsGetLight()
```

**返回：** 光级别（lux）

### sensorsGetStepCounter()
读取步计数器。

```python
sensorsGetStepCounter()
```

**返回：** 步数

### sensorsGetAccuracy()
获取当前传感器精度。

```python
sensorsGetAccuracy()
```

**返回：** 精度值（0-3：UNRELIABLE、ACCURACY_LOW、ACCURACY_MEDIUM、ACCURACY_HIGH）

## 使用示例

```python
import androidhelper
import time

droid = androidhelper.Android()

# 开始感知
droid.startSensingTimed(1, 250)

# 读取传感器 10 次
for i in range(10):
    accel = droid.sensorsReadAccelerometer().result
    print(f"Accel: X={accel[0]:.2f}, Y={accel[1]:.2f}, Z={accel[2]:.2f}")
    time.sleep(0.5)

droid.stopSensing()
```
