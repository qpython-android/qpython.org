# 事件系统

QSL4A 提供了一个事件系统，用于处理来自 Android 的异步事件，如传感器更新、位置变化和自定义广播。

## 事件基础

事件存储在缓冲区中，可以轮询或等待。每个事件包含：
- `name`: 事件类型/名称
- `data`: 事件负载数据
- `time`: 时间戳

## 事件方法

### eventClearBuffer()
清除缓冲区中的所有待处理事件。

```python
eventClearBuffer()
```

**返回：** None

### eventPoll()
轮询缓冲区中的事件。

```python
eventPoll(number_of_events=1)
```

**参数：**
- `number_of_events` (int): 要检索的最大事件数（默认：1）

**返回：** 事件对象列表

### eventWait()
等待任意事件。

```python
eventWait(timeout=None)
```

**参数：**
- `timeout` (int, optional): 超时时间（秒）。None = 永久等待

**返回：** 事件对象，如果超时则返回 None

### eventWaitFor()
等待特定事件。

```python
eventWaitFor(eventName, timeout=None)
```

**参数：**
- `eventName` (str): 要等待的事件名称
- `timeout` (int, optional): 超时时间（秒）

**返回：** 事件对象，如果超时则返回 None

### eventPost()
发布自定义事件。

```python
eventPost(name, data, enqueue=None)
```

**参数：**
- `name` (str): 事件名称
- `data`: 事件数据（任意类型）
- `enqueue` (bool, optional): 如果为 True 则添加到队列

### receiveEvent()
接收事件（阻塞）。

```python
receiveEvent()
```

**返回：** 事件对象

## 广播事件

注册系统广播事件。

### eventRegisterForBroadcast()
注册接收广播事件。

```python
eventRegisterForBroadcast(category, enqueue=True)
```

**参数：**
- `category` (str): 广播类别/动作
- `enqueue` (bool): 添加到事件队列

### eventUnregisterForBroadcast()
取消注册广播事件。

```python
eventUnregisterForBroadcast(category)
```

### eventGetBrodcastCategories()
获取已注册的广播类别。

```python
eventGetBrodcastCategories()
```

**返回：** 已注册类别列表

## 事件分发器)

### startEventDispatcher()
打开一个可以读取已发布事件的套接字。)

```python
startEventDispatcher(port=0)
```

**参数：**
- `port` (int, optional): 监听的端口（默认：0 = 自动选择）

**返回：** 正在监听的端口号

### stopEventDispatcher()
停止事件服务器。)

```python
stopEventDispatcher()
```

## 已废弃方法

### rpcPostEvent()
将事件发布到事件队列。（已废弃，请使用 eventPost）

```python
rpcPostEvent(name, data)
```

**参数：**
- `name` (str): 事件名称
- `data`: 事件数据

## 使用示例

### 基本事件轮询

```python
import androidhelper

droid = androidhelper.Android()

# 清除旧事件
droid.eventClearBuffer()

# 轮询事件
events = droid.eventPoll(5).result
for event in events:
    print(f"Event: {event['name']}, Data: {event['data']}")
```

### 等待事件

```python
# 等待任意事件，带超时
event = droid.eventWait(timeout=10).result
if event:
    print(f"Got event: {event['name']}")
```

### 等待特定事件

```python
# 等待传感器事件
event = droid.eventWaitFor('screen', timeout=5).result
if event:
    print(f"Screen event: {event['data']}")
```

### 发布自定义事件

```python
# 发布自定义事件
droid.eventPost('my_event', {'key': 'value'})

# 等待它
event = droid.eventWaitFor('my_event', timeout=1).result
```

### 广播接收器

```python
# 注册屏幕开关事件
droid.eventRegisterForBroadcast('android.intent.action.SCREEN_ON')
droid.eventRegisterForBroadcast('android.intent.action.SCREEN_OFF')

# 等待屏幕事件
while True:
    event = droid.receiveEvent().result
    if event['name'] == 'android.intent.action.SCREEN_ON':
        print("Screen turned on")
    elif event['name'] == 'android.intent.action.SCREEN_OFF':
        print("Screen turned off")
```

### 传感器事件处理

```python
# 开始感知
droid.startSensingTimed(1, 250)

# 处理传感器事件
for _ in range(100):
    event = droid.eventWait(timeout=1).result
    if event and event['name'] == 'sensors':
        data = event['data']
        print(f"Accel: {data['xforce']}, {data['yforce']}, {data['zforce']}")

droid.stopSensing()
```

## 常见事件类型

| 事件名称 | 描述 | 来源 |
|------------|-------------|--------|
| `sensors` | 传感器数据更新 | startSensing* |
| `location` | GPS 位置更新 | startLocating |
| `phone` | 电话状态变化 | startTrackingPhoneState |
| `signal` | 信号强度变化 | startTrackingSignalStrength |
| `screen` | 截图就绪 | fullGetScreenShot |
| `dialog` | 对话框响应 | dialogShow* |

## 事件数据结构

```python
{
    'name': 'event_name',
    'data': {
        # 事件特定数据
    },
    'time': 1234567890  # 时间戳
}
```
