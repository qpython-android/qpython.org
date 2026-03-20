# Sensor API

Access device sensors including accelerometer, gyroscope, magnetometer, and more.

## Methods

### startSensingTimed()
Start sensor monitoring with time intervals.

```python
startSensingTimed(sensorNumber, delayTime)
```

**Parameters:**
- `sensorNumber` (int): Sensor ID (1-3 typically)
- `delayTime` (int): Delay between readings in milliseconds

### startSensingThreshold()
Start sensor monitoring with threshold trigger.

```python
startSensingThreshold(sensorNumber, threshold, axis)
```

**Parameters:**
- `sensorNumber` (int): Sensor ID
- `threshold` (float): Trigger threshold
- `axis` (int): Axis to monitor (0=X, 1=Y, 2=Z)

### stopSensing()
Stop all sensor monitoring.

```python
stopSensing()
```

### readSensors()
Read current sensor data.

```python
readSensors()
```

**Returns:** Sensor data dict

### sensorsReadAccelerometer()
Read accelerometer values.

```python
sensorsReadAccelerometer()
```

**Returns:** List [X, Y, Z] in m/s²

### sensorsReadGyroscope()
Read gyroscope values.

```python
sensorsReadGyroscope()
```

**Returns:** List [X, Y, Z] in rad/s

### sensorsReadMagnetometer()
Read magnetic field values.

```python
sensorsReadMagnetometer()
```

**Returns:** List [X, Y, Z] in μT

### sensorsReadOrientation()
Read device orientation.

```python
sensorsReadOrientation()
```

**Returns:** List [azimuth, pitch, roll] in degrees

### sensorsGetLight()
Read light sensor value.

```python
sensorsGetLight()
```

**Returns:** Light level in lux

### sensorsGetStepCounter()
Read step counter.

```python
sensorsGetStepCounter()
```

**Returns:** Number of steps

### sensorsGetAccuracy()
Get the current sensor accuracy.

```python
sensorsGetAccuracy()
```

**Returns:** Accuracy value (0-3: UNRELIABLE, ACCURACY_LOW, ACCURACY_MEDIUM, ACCURACY_HIGH)

## Usage Example

```python
import androidhelper
import time

droid = androidhelper.Android()

# Start sensing
droid.startSensingTimed(1, 250)

# Read sensors 10 times
for i in range(10):
    accel = droid.sensorsReadAccelerometer().result
    print(f"Accel: X={accel[0]:.2f}, Y={accel[1]:.2f}, Z={accel[2]:.2f}")
    time.sleep(0.5)

droid.stopSensing()
```
