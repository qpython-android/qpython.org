# QSL4A（Android 脚本层）API 文档

QSL4A 是 QPython 的 Android 脚本层，允许您使用 Python 控制 Android 设备功能。

## 快速开始

```python
import androidhelper

droid = androidhelper.Android()

# 显示 toast 消息
droid.makeToast('Hello QPython!')

# 震动设备
droid.vibrate(500)

# 获取电池电量（先开始监控）
import time
droid.batteryStartMonitoring()
time.sleep(0.5)  # 等待数据
battery = droid.readBatteryData().result
print(f"电池：{battery['level']}%")
```

## 文档结构

### [核心模块](core/)
- [Android 基础](core/android-base.md) - 核心连接和 RPC
- [Intent 系统](core/intent.md) - Android Intent 操作
- [事件系统](core/events.md) - 事件处理和广播

### [UI 组件](ui/)
- [对话框](ui/dialogs.md) - 警报、输入、选择对话框
- [全屏 UI](ui/fullscreen.md) - 自定义布局 UI
- [悬浮窗](ui/floatview.md) - 悬浮窗口
- [辅助功能](ui/accessibility.md) - 屏幕自动化

### [系统](system/)
- [电池](system/battery.md) - 电池监控
- [传感器](system/sensors.md) - 设备传感器
- [应用](system/application.md) - 应用管理
- [系统信息](system/sysinfo.md) - 设备信息
- [设置](system/settings.md) - 系统设置
- [唤醒锁](system/wakelock.md) - 唤醒锁控制
- [QPython 接口](system/qpyinterface.md) - 脚本执行
- [Activity 结果](system/activityresult.md) - Activity 结果处理

### [硬件](hardware/)
- [蓝牙](hardware/bluetooth.md) - 蓝牙操作
- [相机](hardware/camera.md) - 拍照和录像
- [音频/录音器](hardware/recorder.md) - 录音
- [网络摄像头](hardware/webcam.md) - MJPEG 流
- [USB 串口](hardware/usbserial.md) - USB 主机串口

### [连接](connectivity/)
- [WiFi](connectivity/wifi.md) - WiFi 操作
- [位置](connectivity/location.md) - GPS 和位置
- [短信](connectivity/sms.md) - 短信操作
- [电话](connectivity/phone.md) - 打电话和来电信息
- [联系人](connectivity/contacts.md) - 联系人管理
- [信号强度](connectivity/signalstrength.md) - 信号监控
- [FTP 服务器](connectivity/ftp.md) - 内置 FTP 服务器

### [存储](storage/)
- [DocumentFile](storage/documentfile.md) - 文件操作
- [剪贴板](storage/clipboard.md) - 剪贴板操作
- [偏好设置](storage/preferences.md) - 共享偏好设置

### [媒体](media/)
- [媒体播放器](media/mediaplayer.md) - 音频/视频播放
- [图像处理](media/image.md) - 图像操作

### [特殊功能](special/)
- [加密](special/cipher.md) - 加密/解密
- [PGPT AI](special/pgptai.md) - AI 语音服务

## 结果对象

大多数 QSL4A 方法返回一个带有以下属性的 Result 命名元组：
- `id` - 请求 ID
- `result` - 实际结果数据
- `error` - 如果失败则为错误消息

```python
result = droid.getClipboard()
if result.error is None:
    print(result.result)
else:
    print(f"错误：{result.error}")
```
