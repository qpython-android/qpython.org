# WakeLock API

Control device wake locks to keep the CPU or screen on.

## Wake Lock Types

QSL4A provides different wake lock types:

| Type | Description |
|------|-------------|
| Full | CPU on, screen bright, keyboard bright |
| Partial | CPU on only |
| Bright | CPU on, screen bright |
| Dim | CPU on, screen dim |

## Wake Lock Methods

### wakeLockAcquireFull() *ASL4A*
Acquire a full wake lock (CPU on, screen bright, keyboard bright).

```python
wakeLockAcquireFull()
```

### wakeLockAcquirePartial() *ASL4A*
Acquire a partial wake lock (CPU on only).

```python
wakeLockAcquirePartial()
```

### wakeLockAcquireBright() *ASL4A*
Acquire a bright wake lock (CPU on, screen bright).

```python
wakeLockAcquireBright()
```

### wakeLockAcquireDim() *ASL4A*
Acquire a dim wake lock (CPU on, screen dim).

```python
wakeLockAcquireDim()
```

### wakeLockRelease() *ASL4A*
Release the wake lock.

```python
wakeLockRelease()
```

## Usage Example

```python
import androidhelper
import time

droid = androidhelper.Android()

# Acquire full wake lock
droid.wakeLockAcquireFull()

# Do important work while keeping screen on
print("Screen will stay on")
time.sleep(10)

# Release when done
droid.wakeLockRelease()

# Or use partial lock for background tasks
droid.wakeLockAcquirePartial()
# CPU stays on even with screen off
time.sleep(30)
droid.wakeLockRelease()
```

**Note:** Remember to release wake locks when no longer needed to conserve battery.
