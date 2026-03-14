# Application Management

Manage applications and query system information.

## Methods

### getApplicationInfo()
Get information about an app.

```python
getApplicationInfo(packageName=None)
```

**Parameters:**
- `packageName` (str): Package name (None = current app)

**Returns:** App info dict

### getRunningPackages()
List running packages.

```python
getRunningPackages()
```

**Returns:** List of package names

### forceStopPackage()
Force stop an application.

```python
forceStopPackage(packageName)
```

### getPackageVersion()
Get app version name.

```python
getPackageVersion(packageName)
```

### getPackageVersionCode()
Get app version code.

```python
getPackageVersionCode(packageName)
```

### getConstants()
Get class constants.

```python
getConstants(classname)
```

## System Info

### getSysInfo()
Get system information.

```python
getSysInfo()
```

### getAndroidID()
Get Android device ID.

```python
getAndroidID()
```

### getMemoryInfo()
Get memory information.

```python
getMemoryInfo()
```

### getScreenInfo()
Get screen information.

```python
getScreenInfo()
```

### getLocale()
Get device locale.

```python
getLocale()
```

## Usage Example

```python
import androidhelper

droid = androidhelper.Android()

# Get system info
info = droid.getSysInfo().result
print(f"Info: {info}")

# Get app version
version = droid.getPackageVersion("org.qpython.qpy").result
print(f"QPython version: {version}")
```
