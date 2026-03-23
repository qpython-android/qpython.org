# Event System

QSL4A provides an event system for handling asynchronous events from Android, such as sensor updates, location changes, and custom broadcasts.

## Event Basics

Events are stored in a buffer and can be polled or waited for. Each event has:
- `name`: Event type/name
- `data`: Event payload data
- `time`: Timestamp

## Event Methods

### eventClearBuffer()
Clear all pending events from the buffer.

```python
eventClearBuffer()
```

**Returns:** None

### eventPoll()
Poll for events in the buffer.

```python
eventPoll(number_of_events=1)
```

**Parameters:**
- `number_of_events` (int): Maximum events to retrieve (default: 1)

**Returns:** List of event objects

### eventWait()
Wait for any event.

```python
eventWait(timeout=None)
```

**Parameters:**
- `timeout` (int, optional): Timeout in seconds. None = wait forever

**Returns:** Event object or None if timeout

### eventWaitFor()
Wait for a specific event.

```python
eventWaitFor(eventName, timeout=None)
```

**Parameters:**
- `eventName` (str): Name of event to wait for
- `timeout` (int, optional): Timeout in seconds

**Returns:** Event object or None if timeout

### eventPost()
Post a custom event.

```python
eventPost(name, data, enqueue=None)
```

**Parameters:**
- `name` (str): Event name
- `data`: Event data (any type)
- `enqueue` (bool, optional): Add to queue if True

### receiveEvent()
Receive event (blocking).

```python
receiveEvent()
```

**Returns:** Event object

## Broadcast Events

Register for system broadcast events.

### eventRegisterForBroadcast()
Register to receive broadcast events.

```python
eventRegisterForBroadcast(category, enqueue=True)
```

**Parameters:**
- `category` (str): Broadcast category/action
- `enqueue` (bool): Add to event queue

### eventUnregisterForBroadcast()
Unregister from broadcast events.

```python
eventUnregisterForBroadcast(category)
```

### eventGetBrodcastCategories()
Get registered broadcast categories.

```python
eventGetBrodcastCategories()
```

**Returns:** List of registered categories

## Event Dispatcher)

### startEventDispatcher()
Opens up a socket where you can read for events posted.)

```python
startEventDispatcher(port=0)
```

**Parameters:**
- `port` (int, optional): Port to listen on (default: 0 = auto-select)

**Returns:** Port number being listened on

### stopEventDispatcher()
Stops the event server.)

```python
stopEventDispatcher()
```

## Deprecated Methods

### rpcPostEvent()
Post an event to the event queue. (Deprecated, use eventPost)

```python
rpcPostEvent(name, data)
```

**Parameters:**
- `name` (str): Event name
- `data`: Event data

## Usage Examples

### Basic Event Polling

```python
import androidhelper

droid = androidhelper.Android()

# Clear old events
droid.eventClearBuffer()

# Poll for events
events = droid.eventPoll(5).result
for event in events:
    print(f"Event: {event['name']}, Data: {event['data']}")
```

### Waiting for Events

```python
# Wait for any event with timeout
event = droid.eventWait(timeout=10).result
if event:
    print(f"Got event: {event['name']}")
```

### Waiting for Specific Event

```python
# Wait for sensor event
event = droid.eventWaitFor('screen', timeout=5).result
if event:
    print(f"Screen event: {event['data']}")
```

### Posting Custom Events

```python
# Post custom event
droid.eventPost('my_event', {'key': 'value'})

# Wait for it
event = droid.eventWaitFor('my_event', timeout=1).result
```

### Broadcast Receiver

```python
# Register for screen on/off events
droid.eventRegisterForBroadcast('android.intent.action.SCREEN_ON')
droid.eventRegisterForBroadcast('android.intent.action.SCREEN_OFF')

# Wait for screen events
while True:
    event = droid.receiveEvent().result
    if event['name'] == 'android.intent.action.SCREEN_ON':
        print("Screen turned on")
    elif event['name'] == 'android.intent.action.SCREEN_OFF':
        print("Screen turned off")
```

### Sensor Event Handling

```python
# Start sensing
droid.startSensingTimed(1, 250)

# Process sensor events
for _ in range(100):
    event = droid.eventWait(timeout=1).result
    if event and event['name'] == 'sensors':
        data = event['data']
        print(f"Accel: {data['xforce']}, {data['yforce']}, {data['zforce']}")

droid.stopSensing()
```

## Common Event Types

| Event Name | Description | Source |
|------------|-------------|--------|
| `sensors` | Sensor data update | startSensing* |
| `location` | GPS location update | startLocating |
| `phone` | Phone state change | startTrackingPhoneState |
| `signal` | Signal strength change | startTrackingSignalStrength |
| `screen` | Screenshot ready | fullGetScreenShot |
| `dialog` | Dialog response | dialogShow* |

## Event Data Structure

```python
{
    'name': 'event_name',
    'data': {
        # Event-specific data
    },
    'time': 1234567890  # Timestamp
}
```
