# FloatView

Floating window support for overlay UI elements.

## Overview

FloatView allows creating floating windows that stay on top of other applications.

## Methods

### floatViewShow()
Show a floating view.

```python
floatViewShow(layout, x=0, y=0, gravity=None, touchable=True)
```

**Parameters:**
- `layout` (str): View layout definition
- `x` (int): X position
- `y` (int): Y position
- `gravity` (str): Position gravity
- `touchable` (bool): Whether view accepts touch

### floatViewClose()
Close the floating view.

```python
floatViewClose()
```

### floatViewSetText()
Set text in float view.

```python
floatViewSetText(id, text)
```

## Usage Example

```python
import androidhelper

droid = androidhelper.Android()

# Create float view
layout = '{"type":"TextView","id":"msg","text":"Hello"}'
droid.floatViewShow(layout, x=100, y=200)

# Update text
droid.floatViewSetText("msg", "Updated!")

# Close
droid.floatViewClose()
```