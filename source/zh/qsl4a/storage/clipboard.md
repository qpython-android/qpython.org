# 剪贴板 API

复制和粘贴文本到系统剪贴板。

## 方法

### setClipboard()
复制文本到剪贴板。

```python
setClipboard(text)
```

**参数：**
- `text` (str): 要复制的文本

**返回：** 如果成功则为 True

### getClipboard()
从剪贴板获取文本。

```python
getClipboard()
```

**返回：** 剪贴板文本

## 使用示例

```python
import androidhelper

droid = androidhelper.Android()

# 复制到剪贴板
droid.setClipboard("Hello from QPython!")

# 从剪贴板粘贴
text = droid.getClipboard().result
print(f"Clipboard: {text}")
```
