# Location API

Access GPS and network location services.

## Methods

### startLocating()
Start location updates.

```python
startLocating(minUpdateTime=60000, minUpdateDistance=30, updateGnssStatus=False)
```

**Parameters:**
- `minUpdateTime` (int): Minimum time between updates in milliseconds (default: 60000)
- `minUpdateDistance` (float): Minimum distance for update in meters (default: 30)
- `updateGnssStatus` (bool): Enable GNSS status updates (default: False)

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

# Start location updates
droid.startLocating(minUpdateTime=5000, minUpdateDistance=1, updateGnssStatus=False)

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
