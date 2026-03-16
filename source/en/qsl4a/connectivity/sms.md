# SMS API

Send and receive SMS messages.

## Methods

### smsSend()
Send SMS message.

```python
smsSend(destinationAddress, text)
```

**Parameters:**
- `destinationAddress` (str): Phone number
- `text` (str): Message text

### smsGetMessageCount()
Get message count.

```python
smsGetMessageCount(unreadOnly=False, folder="inbox")
```

### smsGetMessageIds()
Get message IDs.

```python
smsGetMessageIds(unreadOnly=False, folder="inbox")
```

### smsGetMessages()
Get message details.

```python
smsGetMessages(unreadOnly=False, folder="inbox", attributes=None)
```

### smsGetMessageById()
Get a specific message by ID.

```python
smsGetMessageById(id, attributes=None)
```

**Parameters:**
- `id` (int): Message ID
- `attributes` (list, optional): Specific attributes to retrieve

**Returns:** Message data dict

### smsGetAttributes()
Get available SMS message attributes.

```python
smsGetAttributes()
```

**Returns:** List of available attribute names

### smsDeleteMessage()
Delete message.

```python
smsDeleteMessage(id)
```

### smsMarkMessageRead()
Mark message as read.

```python
smsMarkMessageRead(ids, read=True)
```

## Usage Example

```python
import androidhelper

droid = androidhelper.Android()

# Send SMS
droid.smsSend("+1234567890", "Hello from QPython!")

# Get unread messages
messages = droid.smsGetMessages(unreadOnly=True).result
for msg in messages:
    print(f"From: {msg['address']}, Text: {msg['body']}")
```
