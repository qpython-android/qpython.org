# Accessibility Service

The Accessibility Service allows automation of UI interactions like clicks, swipes, and system actions.

## Service Control

### accessibilityStartService()
Start the accessibility service.

```python
accessibilityStartService()
```

**Returns:** `True` if successful, `False` otherwise

### accessibilityServiceEnabled()
Check if accessibility service is enabled.

```python
accessibilityServiceEnabled()
```

**Returns:** `True` or `False`

## Screen Interactions

### accessibilityClick()
Click at screen coordinates.

```python
accessibilityClick(x=0, y=0, t=50)
```

**Parameters:**
- `x` (int/float): X coordinate (0=center, decimals supported)
- `y` (int/float): Y coordinate (0=center, decimals supported)
- `t` (int): Press duration in milliseconds (default: 50)

### accessibilitySlide()
Multi-point slide gesture.

```python
accessibilitySlide(XnYn=None, t=None)
```

**Parameters:**
- `XnYn` (list): Coordinates [X1, Y1, X2, Y2, ... Xn, Yn]
- `t` (int): Slide duration (default: 50*n ms)

## System Actions

### accessibilityAction()
Execute system action by code.

```python
accessibilityAction(actionCode)
```

**Action Codes:**
| Code | Constant | Description |
|------|----------|-------------|
| 1 | BACK | Back button |
| 2 | HOME | Home button |
| 3 | RECENTS | Recent apps |
| 4 | NOTIFICATIONS | Open notifications |
| 5 | QUICK_SETTINGS | Open quick settings |
| 6 | POWER_DIALOG | Power menu |
| 7 | TOGGLE_SPLIT_SCREEN | Split screen |
| 8 | LOCK_SCREEN | Lock screen |
| 9 | TAKE_SCREENSHOT | Take screenshot |
| 10 | KEYCODE_HEADSETHOOK | Headset hook |
| 11-14 | ACCESSIBILITY_* | Accessibility buttons |
| 15 | DISMISS_NOTIFICATION_SHADE | Close notifications |
| 16-20 | DPAD_* | Directional pad |
| 21 | MENU | Menu button |
| 22 | MEDIA_PLAY_PAUSE | Play/Pause media |

## Usage Examples

### Click Center Screen

```python
import androidhelper

droid = androidhelper.Android()

# Start service
if not droid.accessibilityServiceEnabled().result:
    droid.accessibilityStartService()

# Click center (0,0 = center)
droid.accessibilityClick(0, 0, t=100)
```

### Swipe Gesture

```python
# Swipe from bottom to top (scroll up)
droid.accessibilitySlide([0, 1.5, 0, -1.5], t=300)
```

### System Navigation

```python
# Press home
droid.accessibilityAction(2)

# Press back
droid.accessibilityAction(1)

# Open notifications
droid.accessibilityAction(4)
```

### Tap Specific Location

```python
# Tap at screen coordinate (500, 800)
droid.accessibilityClick(500, 800)

# Tap at relative position (center horizontally, 3/4 down)
droid.accessibilityClick(0, 1.5)
```
