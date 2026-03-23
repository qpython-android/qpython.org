# 应用管理

管理应用程序、启动应用和查询系统信息。

## 应用程序信息

### getApplicationInfo()
获取应用信息。

```python
getApplicationInfo(packageName=None)
```

**参数：**
- `packageName` (str): 包名（None = 当前应用）

**返回：** 应用信息字典

### getInstalledPackages()
获取已安装包列表。

```python
getInstalledPackages(flag=4)
```

**参数：**
- `flag` (int): 包标志过滤器（默认：4）

**返回：** 已安装包列表

### getRunningPackages()
列出正在运行的包。

```python
getRunningPackages()
```

**返回：** 包名列表

### getLaunchablePackages()
获取可启动包列表。

```python
getLaunchablePackages(needClassName=False)
```

**参数：**
- `needClassName` (bool): 包含主 activity 类名（默认：False）

**返回：** 可启动包名列表或包含类名的字典

## 应用控制

### launch()
启动应用程序。

```python
launch(classname=None, packagename=None, wait=True)
```

**参数：**
- `classname` (str): 主 activity 类名
- `packagename` (str): 包名
- `wait` (bool): 等待启动完成（默认：True）

**返回：** 启动结果

### forceStopPackage()
强制停止应用程序。

```python
forceStopPackage(packageName)
```

**参数：**
- `packageName` (str): 要停止的包名

## 版本信息

### getPackageVersion()
获取应用版本名称。

```python
getPackageVersion(packageName)
```

**返回：** 版本字符串（例如 "3.2.1"）

### getPackageVersionCode()
获取应用版本代码。

```python
getPackageVersionCode(packageName)
```

**返回：** 版本代码整数

### getConstants()
获取类常量。

```python
getConstants(classname)
```

**参数：**
- `classname` (str): 完整类名

**返回：** 常量名和值的字典

## 系统功能

### backgroundProtect()
启用或禁用应用的后台保护。

```python
backgroundProtect(enabled=True)
```

**参数：**
- `enabled` (bool): True 启用保护，False 禁用

### createScriptShortCut()
为脚本创建主屏幕快捷方式。

```python
createScriptShortCut(scriptPath, label=None, iconPath=None, scriptArg=None)
```

**参数：**
- `scriptPath` (str): Python 脚本路径
- `label` (str, optional): 快捷方式标签
- `iconPath` (str, optional): 图标图像路径
- `scriptArg` (str, optional): 传递给脚本的参数

## 设备信息

### getAndroidID()
获取 Android 设备 ID。

```python
getAndroidID()
```

**返回：** 唯一的 Android 设备 ID 字符串

### getSysInfo()
获取系统信息。

```python
getSysInfo()
```

**返回：** 包含系统详情的字典

### getLocale()
获取设备语言环境。

```python
getLocale()
```

**返回：** 语言环境字符串（例如 "en_US"）

### getHarmonyOsInformation()
如果在 HarmonyOS 上运行，获取 HarmonyOS 信息。

```python
getHarmonyOsInformation()
```

**返回：** HarmonyOS 版本信息或 None

### isExternalStorageManager()
检查应用是否有外部存储管理器权限。

```python
isExternalStorageManager()
```

**返回：** 如果有权限则为 True

## 内存和显示

### getMemoryInfo()
获取内存信息。

```python
getMemoryInfo()
```

**返回：** 包含内存统计的字典

### getScreenInfo()
获取屏幕信息。

```python
getScreenInfo()
```

**返回：** 包含宽度、高度、密度的字典

## 权限

### checkPermissions()
检查当前应用权限。

```python
checkPermissions()
```

**返回：** 权限及其状态的字典

### requestPermissions()
向用户请求权限。

```python
requestPermissions(permissions=None)
```

**参数：**
- `permissions` (list, optional): 要请求的权限列表。如果为 None，则请求所有需要的权限。

**返回：** 权限请求结果

## 系统操作

### showScreenLock()
显示屏幕锁定（PIN/图案/密码输入）。

```python
showScreenLock()
```

## 使用示例

```python
import androidhelper

droid = androidhelper.Android()

# 获取系统信息
info = droid.getSysInfo().result
print(f"System: {info}")

# 获取应用版本
version = droid.getPackageVersion("org.qpython.qpy").result
print(f"QPython version: {version}")

# 列出已安装应用
apps = droid.getInstalledPackages().result
print(f"Installed apps: {len(apps)}")

# 启动应用
droid.launch(packagename="com.android.settings")

# 检查权限
perms = droid.checkPermissions().result
print(f"Permissions: {perms}")

# 请求存储权限
droid.requestPermissions(["android.permission.READ_EXTERNAL_STORAGE"])

# 创建快捷方式
droid.createScriptShortCut(
    "/sdcard/my_script.py",
    label="My Script",
    iconPath="/sdcard/icon.png"
)
```
