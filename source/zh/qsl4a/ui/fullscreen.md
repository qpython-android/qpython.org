# 全屏 UI

使用原生 Android 布局创建自定义全屏界面。

## 布局方法

### fullShow()
显示全屏布局。

```python
fullShow(layout, title=None, theme=None)
```

**参数：**
- `layout` (str): JSON 布局定义或布局字符串
- `title` (str, optional): 窗口标题
- `theme` (str, optional): 主题名称

**返回：** 窗口 ID

### fullDismiss()
关闭全屏窗口。

```python
fullDismiss()
```

### fullQuery()
查询所有小部件值。

```python
fullQuery()
```

**返回：** 小部件 ID 和值的字典

### fullQueryDetail()
查询特定小部件详情。

```python
fullQueryDetail(id)
```

## 属性方法

### fullGetProperty()
获取小部件属性。

```python
fullGetProperty(id, property)
```

### fullSetProperty()
设置小部件属性。

```python
fullSetProperty(id, property, value)
```

### fullSetList()
设置列表小部件项目。

```python
fullSetList(id, list, isHtml=False, listType=0)
```

### fullSetList2()
使用资源 ID 设置列表小部件项目。

```python
fullSetList2(id, list, intRes)
```

**参数：**
- `id` (str): 小部件 ID
- `list` (list): 项目列表
- `intRes` (int): 列表项目布局的 Android 资源 ID

### fullSetListSelected()
在列表中设置选中项目。

```python
fullSetListSelected(id, selected)
```

**参数：**
- `id` (str): 列表小部件 ID
- `selected` (int): 要选中的项目索引

### fullGetListSelected()
获取当前选中的列表项目索引。

```python
fullGetListSelected(id)
```

**参数：**
- `id` (str): 列表小部件 ID

**返回：** 选中项目索引

## 批量属性操作

### fullGetProperties()
一次获取多个小部件的属性。

```python
fullGetProperties(ids, property)
```

**参数：**
- `ids` (list): 小部件 ID 列表
- `property` (str): 要获取的属性名

**返回：** 映射小部件 ID 到属性值的字典

### fullSetProperties()
一次设置多个小部件的属性。

```python
fullSetProperties(ids, property, value)
```

**参数：**
- `ids` (list): 小部件 ID 列表
- `property` (str): 要设置的属性名
- `value`: 属性值

## 截图

### fullGetScreenShot()
捕获全屏截图。

```python
fullGetScreenShot(path=None)
```

**参数：**
- `path` (str, optional): 保存路径。如果为 None，则在事件中返回

**返回：** 包含截图数据的事件

## 使用示例

```python
import androidhelper

droid = androidhelper.Android()

# 定义布局
layout = '''
{ "type": "LinearLayout", "orientation": "vertical",
  "children": [
    { "type": "TextView", "id": "title", "text": "Hello" },
    { "type": "Button", "id": "btn", "text": "Click Me" }
  ]
}
'''

# 显示布局
droid.fullShow(layout, "My App")

# 查询按钮点击
event = droid.eventWaitFor('click', timeout=10)
if event.result:
    widget_id = event.result['data']['id']
    if widget_id == 'btn':
        print("Button clicked!")

droid.fullDismiss()
```
