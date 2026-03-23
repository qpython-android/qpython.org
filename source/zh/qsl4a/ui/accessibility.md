# 无障碍服务

无障碍服务允许自动化 UI 交互，如点击、滑动和系统操作。

## 服务控制

### accessibilityStartService()
启动无障碍服务。

```python
accessibilityStartService()
```

**返回：** 如果成功则为 `True`，否则为 `False`

### accessibilityServiceEnabled()
检查无障碍服务是否已启用。

```python
accessibilityServiceEnabled()
```

**返回：** `True` 或 `False`

## 屏幕交互

### accessibilityClick()
在屏幕坐标处点击。

```python
accessibilityClick(x=0, y=0, t=50)
```

**参数：**
- `x` (int/float): X 坐标（0=居中，支持小数）
- `y` (int/float): Y 坐标（0=居中，支持小数）
- `t` (int): 按住时长（毫秒）（默认：50）

### accessibilitySlide()
多点滑动手势。

```python
accessibilitySlide(XnYn=None, t=None)
```

**参数：**
- `XnYn` (list): 坐标 [X1, Y1, X2, Y2, ... Xn, Yn]
- `t` (int): 滑动时长（默认：50*n 毫秒）

## 系统操作

### accessibilityAction()
按代码执行系统操作。

```python
accessibilityAction(actionCode)
```

**操作代码：**
| 代码 | 常量 | 描述 |
|------|----------|-------------|
| 1 | BACK | 返回按钮 |
| 2 | HOME | 主屏幕按钮 |
| 3 | RECENTS | 最近应用 |
| 4 | NOTIFICATIONS | 打开通知 |
| 5 | QUICK_SETTINGS | 打开快速设置 |
| 6 | POWER_DIALOG | 电源菜单 |
| 7 | TOGGLE_SPLIT_SCREEN | 分屏 |
| 8 | LOCK_SCREEN | 锁屏 |
| 9 | TAKE_SCREENSHOT | 截图 |
| 10 | KEYCODE_HEADSETHOOK | 耳机挂钩 |
| 11-14 | ACCESSIBILITY_* | 无障碍按钮 |
| 15 | DISMISS_NOTIFICATION_SHADE | 关闭通知栏 |
| 16-20 | DPAD_* | 方向键 |
| 21 | MENU | 菜单按钮 |
| 22 | MEDIA_PLAY_PAUSE | 播放/暂停媒体 |

## 使用示例

### 点击屏幕中心

```python
import androidhelper

droid = androidhelper.Android()

# 启动服务
if not droid.accessibilityServiceEnabled().result:
    droid.accessibilityStartService()

# 点击中心（0,0 = 中心）
droid.accessibilityClick(0, 0, t=100)
```

### 滑动手势

```python
# 从下往上滑动（向上滚动）
droid.accessibilitySlide([0, 1.5, 0, -1.5], t=300)
```

### 系统导航

```python
# 按主屏幕
droid.accessibilityAction(2)

# 按返回
droid.accessibilityAction(1)

# 打开通知
droid.accessibilityAction(4)
```

### 点击特定位置

```python
# 点击屏幕坐标 (500, 800)
droid.accessibilityClick(500, 800)

# 点击相对位置（水平居中，垂直 3/4 处）
droid.accessibilityClick(0, 1.5)
```
