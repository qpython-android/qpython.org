# FloatView

Floating window support for overlay UI elements that stay on top of other applications.

## Methods

### floatView()
Show or modify a floating view.

```python
floatView(Args=None)
```

**Parameters:**
- `Args` (dict): Configuration dictionary with the following keys:
  - `index` (int): Float view index (-1 to create new, >=0 to modify existing)
  - `text` (str): Text content to display
  - `html` (str): HTML content (used if text is omitted)
  - `width` (int): View width in pixels (default: 300)
  - `height` (int): View height in pixels (default: 150)
  - `x` (int): X position (0 = center, positive/negative for offset)
  - `y` (int): Y position (0 = center, positive/negative for offset)
  - `backColor` (str): Background color in ARGB hex (default: '7f7f7f7f')
  - `textColor` (str): Text color in ARGB hex (default: 'ff000000')
  - `textSize` (int): Text size (default: 10)
  - `textAlign` (int): Text alignment (0 = inherit)
  - `script` (str): Script path to run after long click close
  - `arg`: Script argument
  - `clickRemove` (bool): Enable click to remove (default: True)
  - `flag` (int): Window flag (default: 40 - touchable)

**Returns:** Current chain list length

### floatViewCount()
Get the number of active float views.

```python
floatViewCount()
```

**Returns:** Number of float views

### floatViewResult()
Get the result/status of a float view.

```python
floatViewResult(index=-1)
```

**Parameters:**
- `index` (int): Float view index (default: -1, returns last operation result)

**Returns:** Dict with operation details including:
  - `x`, `y`: Position
  - `time`: Timestamp
  - `operation`: Operation type ('initial', 'move', etc.)
  - `index`: View index
  - `removed`: True if view was removed

### floatViewRemove()
Remove a float view.

```python
floatViewRemove(index=-1)
```

**Parameters:**
- `index` (int): Index of view to remove (default: -1 removes the last one)

**Returns:** 1 if successful, 0 otherwise

## Constants

- `floatView.INDEX_NEW = -1` - Create new float view
- `floatView.FLAG_DEFAULT_TOUCHABLE = 40` - Default touchable flag
- `floatView.TEXT_ALIGNMENT_INHERIT = 0`
- `floatView.TEXT_ALIGNMENT_CENTER` - Center text alignment

## Usage Examples

### Basic Float View

```python
import androidhelper
from androidhelper import Android

droid = androidhelper.Android()

# Create a simple float view
droid.floatView({
    'index': -1,  # Create new
    'text': 'Hello World',
    'width': 400,
    'height': 300,
    'x': -300,  # Offset from center
    'y': -400,
    'backColor': 'ff0000',  # Red background
    'textColor': '0000ff',  # Blue text
    'textSize': 16,
    'textAlign': droid.floatView.TEXT_ALIGNMENT_CENTER
})

# Check count
print(f"Float views: {droid.floatViewCount().result}")

# Get result
result = droid.floatViewResult().result
print(f"View info: {result}")

# Remove the float view
droid.floatViewRemove(0)
```

### HTML Content

```python
# Create float view with HTML content
droid.floatView({
    'text': '',  # Empty text to use HTML
    'html': '<h1>Title</h1><p>Rich <b>HTML</b> content</p>',
    'width': 500,
    'height': 400
})
```

### Modify Existing View

```python
# Create initial view
droid.floatView({'text': 'Initial Text', 'width': 300, 'height': 150})

# Modify the same view (index 0)
droid.floatView({
    'index': 0,
    'text': 'Updated Text!',
    'backColor': '7f00ff00'  # Green background
})

# Check the move/change result
result = droid.floatViewResult(0).result
print(f"Operation: {result.get('operation')}, Position: ({result.get('x')}, {result.get('y')})")
```

### Multiple Float Views

```python
# Create multiple views
for i in range(3):
    droid.floatView({
        'index': -1,
        'text': f'View {i}',
        'x': i * 100 - 150,
        'y': i * 100 - 150,
        'backColor': f'{i}f{i}f{i}f'
    })

print(f"Total views: {droid.floatViewCount().result}")

# Remove all views
while droid.floatViewCount().result > 0:
    droid.floatViewRemove()
```

### With Script Callback

```python
# Create float view that runs script on close
droid.floatView({
    'text': 'Click to close and run script',
    'script': '/sdcard/my_script.py',
    'arg': 'hello from float view',
    'clickRemove': True
})
```
