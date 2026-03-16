# Application Management

Manage applications, launch apps, and query system information.

## Application Information

### getApplicationInfo()
Get information about an app.

```python
getApplicationInfo(packageName=None)
```

**Parameters:**
- `packageName` (str): Package name (None = current app)

**Returns:** App info dict

### getInstalledPackages()
Get list of installed packages.

```python
getInstalledPackages(flag=4)
```

**Parameters:**
- `flag` (int): Package flag filter (default: 4)

**Returns:** List of installed packages

### getRunningPackages()
List running packages.

```python
getRunningPackages()
```

**Returns:** List of package names

### getLaunchablePackages()
Get list of launchable packages.

```python
getLaunchablePackages(needClassName=False)
```

**Parameters:**
- `needClassName` (bool): Include main activity class name (default: False)

**Returns:** List of launchable package names or dict with class names

## Application Control

### launch()
Launch an application.

```python
launch(classname=None, packagename=None, wait=True)
```

**Parameters:**
- `classname` (str): Main activity class name
- `packagename` (str): Package name
- `wait` (bool): Wait for launch to complete (default: True)

**Returns:** Launch result

### forceStopPackage()
Force stop an application.

```python
forceStopPackage(packageName)
```

**Parameters:**
- `packageName` (str): Package name to stop

## Version Information

### getPackageVersion()
Get app version name.

```python
getPackageVersion(packageName)
```

**Returns:** Version string (e.g., "3.2.1")

### getPackageVersionCode()
Get app version code.

```python
getPackageVersionCode(packageName)
```

**Returns:** Version code integer

### getConstants()
Get class constants.

```python
getConstants(classname)
```

**Parameters:**
- `classname` (str): Full class name

**Returns:** Dict of constant names and values

## System Features

### backgroundProtect()
Enable or disable background protection for the app.

```python
backgroundProtect(enabled=True)
```

**Parameters:**
- `enabled` (bool): True to enable protection, False to disable

### createScriptShortCut()
Create a home screen shortcut for a script.

```python
createScriptShortCut(scriptPath, label=None, iconPath=None, scriptArg=None)
```

**Parameters:**
- `scriptPath` (str): Path to the Python script
- `label` (str, optional): Shortcut label
- `iconPath` (str, optional): Path to icon image
- `scriptArg` (str, optional): Argument to pass to script

## Device Information

### getAndroidID()
Get Android device ID.

```python
getAndroidID()
```

**Returns:** Unique Android device ID string

### getSysInfo()
Get system information.

```python
getSysInfo()
```

**Returns:** Dict with system details

### getLocale()
Get device locale.

```python
getLocale()
```

**Returns:** Locale string (e.g., "en_US")

### getHarmonyOsInformation()
Get HarmonyOS information if running on HarmonyOS.

```python
getHarmonyOsInformation()
```

**Returns:** HarmonyOS version info or None

### isExternalStorageManager()
Check if app has external storage manager permission.

```python
isExternalStorageManager()
```

**Returns:** True if has permission

## Memory and Display

### getMemoryInfo()
Get memory information.

```python
getMemoryInfo()
```

**Returns:** Dict with memory stats

### getScreenInfo()
Get screen information.

```python
getScreenInfo()
```

**Returns:** Dict with width, height, density

## Permissions

### checkPermissions()
Check current app permissions.

```python
checkPermissions()
```

**Returns:** Dict of permissions and their status

### requestPermissions()
Request permissions from the user.

```python
requestPermissions(permissions=None)
```

**Parameters:**
- `permissions` (list, optional): List of permissions to request. If None, requests all needed permissions.

**Returns:** Result of permission request

## System Actions

### showScreenLock()
Show screen lock (PIN/pattern/password entry).

```python
showScreenLock()
```

## Usage Example

```python
import androidhelper

droid = androidhelper.Android()

# Get system info
info = droid.getSysInfo().result
print(f"System: {info}")

# Get app version
version = droid.getPackageVersion("org.qpython.qpy").result
print(f"QPython version: {version}")

# List installed apps
apps = droid.getInstalledPackages().result
print(f"Installed apps: {len(apps)}")

# Launch an app
droid.launch(packagename="com.android.settings")

# Check permissions
perms = droid.checkPermissions().result
print(f"Permissions: {perms}")

# Request storage permission
droid.requestPermissions(["android.permission.READ_EXTERNAL_STORAGE"])

# Create shortcut
droid.createScriptShortCut(
    "/sdcard/my_script.py",
    label="My Script",
    iconPath="/sdcard/icon.png"
)
```
