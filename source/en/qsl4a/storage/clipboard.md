# Clipboard API

Copy and paste text to system clipboard.

## Methods

### setClipboard()
Copy text to clipboard.

```python
setClipboard(text)
```

**Parameters:**
- `text` (str): Text to copy

**Returns:** True if success

### getClipboard()
Get text from clipboard.

```python
getClipboard()
```

**Returns:** Clipboard text

## Usage Example

```python
import androidhelper

droid = androidhelper.Android()

# Copy to clipboard
droid.setClipboard("Hello from QPython!")

# Paste from clipboard
text = droid.getClipboard().result
print(f"Clipboard: {text}")
```
