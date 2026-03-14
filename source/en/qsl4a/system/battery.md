# Battery API

Monitor device battery status and health.

## Methods

### readBatteryData()
Get complete battery information.

```python
readBatteryData()
```

**Returns:** Dict with battery data

### batteryStartMonitoring()
Start battery monitoring.

```python
batteryStartMonitoring()
```

### batteryStopMonitoring()
Stop battery monitoring.

```python
batteryStopMonitoring()
```

### batteryGetLevel()
Get battery percentage.

```python
batteryGetLevel()
```

**Returns:** Int (0-100)

### batteryGetStatus()
Get charging status.

```python
batteryGetStatus()
```

**Returns:**
- 1: Unknown
- 2: Charging
- 3: Discharging
- 4: Not charging
- 5: Full

### batteryGetPlugType()
Get power source.

```python
batteryGetPlugType()
```

**Returns:**
- -1: Unknown
- 0: Unplugged
- 1: AC charger
- 2: USB port

### batteryGetHealth()
Get battery health.

```python
batteryGetHealth()
```

**Returns:**
- 1: Unknown
- 2: Good
- 3: Overheat
- 4: Dead
- 5: Over voltage
- 6: Unspecified failure

## Usage Example

```python
import androidhelper

droid = androidhelper.Android()

# Get battery level
level = droid.batteryGetLevel().result
print(f"Battery: {level}%")
```