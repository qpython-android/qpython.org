# 浮动视图

浮动窗口支持，用于在其他应用程序上方保持显示的覆盖 UI 元素。

## 方法

### floatView()
显示或修改浮动视图。

```python
floatView(Args=None)
```

**参数：**
- `Args` (dict): 配置字典，包含以下键：
  - `index` (int): 浮动视图索引（-1 创建新的，>=0 修改现有的）
  - `text` (str): 要显示的文本内容
  - `html` (str): HTML 内容（如果省略 text 则使用）
  - `width` (int): 视图宽度（像素）（默认：300）
  - `height` (int): 视图高度（像素）（默认：150）
  - `x` (int): X 位置（0 = 居中，正/负表示偏移）
  - `y` (int): Y 位置（0 = 居中，正/负表示偏移）
  - `backColor` (str): ARGB 十六进制背景色（默认：'7f7f7f7f'）
  - `textColor` (str): ARGB 十六进制文本色（默认：'ff000000'）
  - `textSize` (int): 文本大小（默认：10）
  - `textAlign` (int): 文本对齐（0 = 继承）
  - `script` (str): 长按关闭后运行的脚本路径
  - `arg`: 脚本参数
  - `clickRemove` (bool): 启用点击移除（默认：True）
  - `flag` (int): 窗口标志（默认：40 - 可触摸）

**返回：** 当前链列表长度

### floatViewCount()
获取活动浮动视图的数量。

```python
floatViewCount()
```

**返回：** 浮动视图数量

### floatViewResult()
获取浮动视图的结果/状态。

```python
floatViewResult(index=-1)
```

**参数：**
- `index` (int): 浮动视图索引（默认：-1，返回最后操作结果）

**返回：** 包含操作详情的字典，包括：
  - `x`, `y`: 位置
  - `time`: 时间戳
  - `operation`: 操作类型（'initial'、'move' 等）
  - `index`: 视图索引
  - `removed`: 如果视图被移除则为 True

### floatViewRemove()
移除浮动视图。

```python
floatViewRemove(index=-1)
```

**参数：**
- `index` (int): 要移除的视图索引（默认：-1 移除最后一个）

**返回：** 如果成功则为 1，否则为 0

## 常量

- `floatView.INDEX_NEW = -1` - 创建新的浮动视图
- `floatView.FLAG_DEFAULT_TOUCHABLE = 40` - 默认可触摸标志
- `floatView.TEXT_ALIGNMENT_INHERIT = 0`
- `floatView.TEXT_ALIGNMENT_CENTER` - 居中文本对齐

## 使用示例

### 基本浮动视图

```python
import androidhelper
from androidhelper import Android

droid = androidhelper.Android()

# 创建简单浮动视图
droid.floatView({
    'index': -1,  # 创建新的
    'text': 'Hello World',
    'width': 400,
    'height': 300,
    'x': -300,  # 从中心偏移
    'y': -400,
    'backColor': 'ff0000',  # 红色背景
    'textColor': '0000ff',  # 蓝色文本
    'textSize': 16,
    'textAlign': droid.floatView.TEXT_ALIGNMENT_CENTER
})

# 检查数量
print(f"Float views: {droid.floatViewCount().result}")

# 获取结果
result = droid.floatViewResult().result
print(f"View info: {result}")

# 移除浮动视图
droid.floatViewRemove(0)
```

### HTML 内容

```python
# 创建带 HTML 内容的浮动视图
droid.floatView({
    'text': '',  # 空文本以使用 HTML
    'html': '<h1>Title</h1><p>Rich <b>HTML</b> content</p>',
    'width': 500,
    'height': 400
})
```

### 修改现有视图

```python
# 创建初始视图
droid.floatView({'text': 'Initial Text', 'width': 300, 'height': 150})

# 修改同一视图（索引 0）
droid.floatView({
    'index': 0,
    'text': 'Updated Text!',
    'backColor': '7f00ff00'  # 绿色背景
})

# 检查移动/更改结果
result = droid.floatViewResult(0).result
print(f"Operation: {result.get('operation')}, Position: ({result.get('x')}, {result.get('y')})")
```

### 多个浮动视图

```python
# 创建多个视图
for i in range(3):
    droid.floatView({
        'index': -1,
        'text': f'View {i}',
        'x': i * 100 - 150,
        'y': i * 100 - 150,
        'backColor': f'{i}f{i}f{i}f'
    })

print(f"Total views: {droid.floatViewCount().result}")

# 移除所有视图
while droid.floatViewCount().result > 0:
    droid.floatViewRemove()
```

### 带脚本回调

```python
# 创建关闭时运行脚本的浮动视图
droid.floatView({
    'text': 'Click to close and run script',
    'script': '/sdcard/my_script.py',
    'arg': 'hello from float view',
    'clickRemove': True
})
```
