# 联系人 API

访问和管理设备联系人。

## 选择联系人

### pickContact() *ASL4A*
显示联系人列表以供选择。

```python
pickContact()
```

**返回：** 包含联系人 URI 的 Intent

### pickPhone() *ASL4A*
显示电话号码列表以供选择。

```python
pickPhone()
```

**返回：** 选中的电话号码字符串

## 联系人查询

### contactsGet() *ASL4A*
获取所有联系人。

```python
contactsGet(attributes=None)
```

**参数：**
- `attributes` (list, optional): 要检索的特定属性

**返回：** 联系人 JSONObject 列表

### contactsGetById() *ASL4A*
通过 ID 获取联系人。

```python
contactsGetById(id, attributes=None)
```

**参数：**
- `id` (int): 联系人 ID
- `attributes` (list, optional): 要检索的特定属性

**返回：** JSONObject 联系人数据

### contactsGetCount() *ASL4A*
获取联系人总数。

```python
contactsGetCount()
```

**返回：** 整数计数

### contactsGetIds() *ASL4A*
获取所有联系人 ID。

```python
contactsGetIds()
```

**返回：** 联系人 ID 整数列表

### contactsGetAttributes() *ASL4A*
获取所有可能的联系人属性。

```python
contactsGetAttributes()
```

**返回：** 属性名称列表

## 内容查询

### queryContent() *ASL4A*
使用自定义参数查询内容解析器。

```python
queryContent(uri, attributes=None, selection=None, selectionArgs=None, order=None)
```

**参数：**
- `uri` (str): 内容 URI
- `attributes` (list, optional): 要检索的属性
- `selection` (str, optional): WHERE 子句
- `selectionArgs` (list, optional): 选择参数
- `order` (str, optional): ORDER BY 子句

**返回：** JSONObject 结果列表

### queryAttributes() *ASL4A*
获取内容 URI 的属性。

```python
queryAttributes(uri)
```

**参数：**
- `uri` (str): 内容 URI

**返回：** 属性名称的 JSONArray

## 使用示例

```python
import androidhelper

droid = androidhelper.Android()

# 选择联系人
contact_uri = droid.pickContact().result
print(f"Selected contact: {contact_uri}")

# 选择电话号码
phone = droid.pickPhone().result
print(f"Selected phone: {phone}")

# 获取所有联系人
contacts = droid.contactsGet().result
print(f"Total contacts: {len(contacts)}")

# 通过 ID 获取联系人
contact = droid.contactsGetById(1).result
print(f"Contact: {contact}")

# 获取联系人属性
attrs = droid.contactsGetAttributes().result
print(f"Available attributes: {attrs}")
```
