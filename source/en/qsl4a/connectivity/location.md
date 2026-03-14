# Location API

Access GPS and network location services.

## Methods

### startLocating()
Start location updates.

```python
startLocating(provider="gps", minUpdateDistance=1, minUpdateTime=5000)
```

**Parameters:**
- `provider` (str): "gps" or "network"
- `minUpdateDistance` (float): Minimum distance for update (meters)
- `minUpdateTime` (int): Minimum time between updates (ms)

### stopLocating()
Stop location updates.

```python
stopLocating()
```

### readLocation()
Get last known location.

```python
readLocation()
```

**Returns:** Location data dict

### getLastKnownLocation()
Get cached location.

```python
getLastKnownLocation()
```

**Returns:** Location from all providers

### geocode()
Convert address to coordinates.

```python
geocode(address, maxResults=1)
```

## Usage Example

```python
import androidhelper
import time

droid = androidhelper.Android()

# Start GPS
droid.startLocating("gps", 1, 5000)

# Wait for fix
time.sleep(10)

# Get location
loc = droid.readLocation().result
if loc:
    lat = loc['latitude']
    lon = loc['longitude']
    print(f"Location: {lat}, {lon}")

droid.stopLocating()
```
