# SMS API

发送和接收 SMS 消息。

## 方法

### smsSend()
发送 SMS 消息。

```python
smsSend(destinationAddress, text)
```

**参数：**
- `destinationAddress` (str): 电话号码
- `text` (str): 消息文本

### smsGetMessageCount()
获取消息数量。

```python
smsGetMessageCount(unreadOnly=False, folder="inbox")
```

### smsGetMessageIds()
获取消息 ID。

```python
smsGetMessageIds(unreadOnly=False, folder="inbox")
```

### smsGetMessages()
获取消息详情。

```python
smsGetMessages(unreadOnly=False, folder="inbox", attributes=None)
```

### smsGetMessageById()
通过 ID 获取特定消息。

```python
smsGetMessageById(id, attributes=None)
```

**参数：**
- `id` (int): 消息 ID
- `attributes` (list, optional): 要检索的特定属性

**返回：** 消息数据字典

### smsGetAttributes()
获取可用的 SMS 消息属性。

```python
smsGetAttributes()
```

**返回：** 可用属性名称列表

### smsDeleteMessage()
删除消息。

```python
smsDeleteMessage(id)
```

### smsMarkMessageRead()
将消息标记为已读。

```python
smsMarkMessageRead(ids, read=True)
```

## 使用示例

```python
import androidhelper

droid = androidhelper.Android()

# 发送 SMS
droid.smsSend("+1234567890", "Hello from QPython!")

# 获取未读消息
messages = droid.smsGetMessages(unreadOnly=True).result
for msg in messages:
    print(f"From: {msg['address']}, Text: {msg['body']}")
```
