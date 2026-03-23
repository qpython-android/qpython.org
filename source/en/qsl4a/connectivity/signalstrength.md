# Signal Strength API

Monitor cellular and wireless signal strength.

## Signal Strength Methods

### startTrackingSignalStrengths()
Start tracking signal strength changes. Generates 'signal_strengths' events.

```python
startTrackingSignalStrengths()
```

### stopTrackingSignalStrengths()
Stop tracking signal strengths.

```python
stopTrackingSignalStrengths()
```

### readSignalStrengths()
Read the current signal strengths.

```python
readSignalStrengths()
```

**Returns:** Bundle with signal strength data

### getTelephoneSignalStrengthLevel()
Get the telephone signal strength as a level (0-4).

```python
getTelephoneSignalStrengthLevel()
```

**Returns:** Integer level (0=none, 1=poor, 2=fair, 3=good, 4=excellent)

### getTelephoneSignalStrengthDetail()
Get detailed telephone signal strength information.

```python
getTelephoneSignalStrengthDetail()
```

**Returns:** String with detailed signal info

## Usage Example

```python
import androidhelper
import time

droid = androidhelper.Android()

# Start tracking signal strength
droid.startTrackingSignalStrengths()

# Wait for signal updates
time.sleep(5)

# Read current signal strength
signal = droid.readSignalStrengths().result
print(f"Signal: {signal}")

# Get level directly
level = droid.getTelephoneSignalStrengthLevel().result
print(f"Signal level: {level}/4")

droid.stopTrackingSignalStrengths()
```
