# FullScreen UI

Create custom fullscreen interfaces with native Android layouts.

## Layout Methods

### fullShow()
Show a fullscreen layout.

```python
fullShow(layout, title=None, theme=None)
```

**Parameters:**
- `layout` (str): JSON layout definition or layout string
- `title` (str, optional): Window title
- `theme` (str, optional): Theme name

**Returns:** Window ID

### fullDismiss()
Close fullscreen window.

```python
fullDismiss()
```

### fullQuery()
Query all widget values.

```python
fullQuery()
```

**Returns:** Dict of widget IDs and values

### fullQueryDetail()
Query specific widget details.

```python
fullQueryDetail(id)
```

## Property Methods

### fullGetProperty()
Get widget property.

```python
fullGetProperty(id, property)
```

### fullSetProperty()
Set widget property.

```python
fullSetProperty(id, property, value)
```

### fullSetList()
Set list widget items.

```python
fullSetList(id, list, isHtml=False, listType=0)
```

### fullSetList2()
Set list widget items with resource ID.

```python
fullSetList2(id, list, intRes)
```

**Parameters:**
- `id` (str): Widget ID
- `list` (list): List of items
- `intRes` (int): Android resource ID for list item layout

### fullSetListSelected()
Set selected item in a list.

```python
fullSetListSelected(id, selected)
```

**Parameters:**
- `id` (str): List widget ID
- `selected` (int): Index of item to select

### fullGetListSelected()
Get the currently selected list item index.

```python
fullGetListSelected(id)
```

**Parameters:**
- `id` (str): List widget ID

**Returns:** Selected item index

## Batch Property Operations

### fullGetProperties()
Get properties for multiple widgets at once.

```python
fullGetProperties(ids, property)
```

**Parameters:**
- `ids` (list): List of widget IDs
- `property` (str): Property name to get

**Returns:** Dict mapping widget IDs to property values

### fullSetProperties()
Set property for multiple widgets at once.

```python
fullSetProperties(ids, property, value)
```

**Parameters:**
- `ids` (list): List of widget IDs
- `property` (str): Property name to set
- `value`: Property value

## Screenshot

### fullGetScreenShot()
Capture fullscreen screenshot.

```python
fullGetScreenShot(path=None)
```

**Parameters:**
- `path` (str, optional): Save path. If None, returns in event

**Returns:** Event with screenshot data

## Usage Example

```python
import androidhelper

droid = androidhelper.Android()

# Define layout
layout = '''
{ "type": "LinearLayout", "orientation": "vertical",
  "children": [
    { "type": "TextView", "id": "title", "text": "Hello" },
    { "type": "Button", "id": "btn", "text": "Click Me" }
  ]
}
'''

# Show layout
droid.fullShow(layout, "My App")

# Query button click
event = droid.eventWaitFor('click', timeout=10)
if event.result:
    widget_id = event.result['data']['id']
    if widget_id == 'btn':
        print("Button clicked!")

droid.fullDismiss()
```