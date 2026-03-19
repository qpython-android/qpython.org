# Intent System

Android Intents are used to start activities, send broadcasts, and communicate between apps. QSL4A provides full Intent support through the `Intent` module.

## Module Import

```python
import androidhelper
don = androidhelper.Android()
```

## Intent Constants

Access via `droid.Intent`:

### Actions

| Constant | Value | Usage |
|----------|-------|-------|
| `ACTION_MAIN` | android.intent.action.MAIN | App entry point |
| `ACTION_VIEW` | android.intent.action.VIEW | View content |
| `ACTION_EDIT` | android.intent.action.EDIT | Edit content |
| `ACTION_PICK` | android.intent.action.PICK | Pick item |
| `ACTION_SEND` | android.intent.action.SEND | Share content |
| `ACTION_SEARCH` | android.intent.action.SEARCH | Search |

### Flags

| Constant | Value | Usage |
|----------|-------|-------|
| `FLAG_ACTIVITY_NEW_TASK` | 268435456 | Start new task |
| `FLAG_ACTIVITY_CLEAR_TASK` | 32768 | Clear task stack |
| `FLAG_ACTIVITY_NEW_DOCUMENT` | 524288 | New document mode |

### Extras

| Constant | Usage |
|----------|-------|
| `EXTRA_TEXT` | Text content |
| `EXTRA_STREAM` | File URI |
| `EXTRA_SUBJECT` | Subject line |
| `EXTRA_EMAIL` | Email address |

## Core Methods

### makeIntent()
Create an Intent object.

```python
makeIntent(action, uri=None, type=None, extras=None, categories=None,
           packagename=None, classname=None, flags=None)
```

**Parameters:**
- `action` (str): Intent action (e.g., `droid.Intent.ACTION_VIEW`)
- `uri` (str, optional): Data URI
- `type` (str, optional): MIME type
- `extras` (dict, optional): Extra data
- `categories` (list, optional): Intent categories
- `packagename` (str, optional): Target package
- `classname` (str, optional): Target class
- `flags` (int, optional): Intent flags

**Returns:** Intent object

### startActivityIntent()
Start an Activity with an Intent.

```python
startActivityIntent(intent, wait=None)
```

**Parameters:**
- `intent`: Intent object from makeIntent()
- `wait` (bool, optional): Block until activity closes

### startActivityForResultIntent()
Start activity and wait for result.

```python
startActivityForResultIntent(intent)
```

**Returns:** Activity result

### sendBroadcastIntent()
Send a broadcast.

```python
sendBroadcastIntent(intent)
```

### view()
View content by URI.

```python
view(uri, type=None, extras=None)
```

### pick()
Pick content from URI.

```python
pick(uri)
```

## Common Intent Methods *ASL4A*

### scanBarcode() *ASL4A*
Launch the barcode scanner.

```python
scanBarcode()
```

**Returns:** Scanned barcode string

### send() *ASL4A*
Send content via share intent.

```python
send(type, content)
```

**Parameters:**
- `type` (str): MIME type
- `content` (str): Content to share

### sendText() *ASL4A*
Send text content.

```python
sendText(text)
```

**Parameters:**
- `text` (str): Text to send

### sendEmail() *ASL4A*
Send an email.

```python
sendEmail(to, subject, body, attachment=None)
```

**Parameters:**
- `to` (str or list): Recipient email address(es)
- `subject` (str): Email subject
- `body` (str): Email body
- `attachment` (str, optional): Attachment file path

### pathToUri() *ASL4A*
Convert file path to content URI.

```python
pathToUri(path)
```

**Parameters:**
- `path` (str): File path

**Returns:** Content URI string

### openFile() *ASL4A*
Open a file with appropriate app.

```python
openFile(path)
```

**Parameters:**
- `path` (str): File path to open

### sendFile() *ASL4A*
Send a file via share intent.

```python
sendFile(path)
```

**Parameters:**
- `path` (str): File path to send

### getPathType() *ASL4A*
Get the MIME type for a file path.

```python
getPathType(path)
```

**Parameters:**
- `path` (str): File path

**Returns:** MIME type string

### viewMap() *ASL4A*
Open map at a location.

```python
viewMap(latitude, longitude)
```

**Parameters:**
- `latitude` (float): Latitude
- `longitude` (float): Longitude

### viewContacts() *ASL4A*
Open the contacts app.

```python
viewContacts()
```

### search() *ASL4A*
Perform a web search.

```python
search(query)
```

**Parameters:**
- `query` (str): Search query

### viewHtml() *ASL4A*
View HTML content.

```python
viewHtml(content, encoding=None)
```

**Parameters:**
- `content` (str): HTML content
- `encoding` (str, optional): Character encoding

### webViewShow() *ASL4A*
Display web content in WebView. Deprecated, use viewHtml.

```python
webViewShow(url)
```

**Parameters:**
- `url` (str): Web page URL

### editorOpen() *ASL4A*
Open a text editor.

```python
editorOpen(path=None, create=False)
```

**Parameters:**
- `path` (str, optional): File path to edit
- `create` (bool, optional): Create if doesn't exist

## Helper Class: Uri

Create URI objects for Intents:

```python
from androidhelper.Intent import Uri

uri = Uri("file:///sdcard/test.txt")
```

## Usage Examples

### Open Web Page

```python
intent = droid.makeIntent(
    action=droid.Intent.ACTION_VIEW,
    uri="http://www.example.com"
).result
droid.startActivityIntent(intent)
```

### Share Text

```python
intent = droid.makeIntent(
    action=droid.Intent.ACTION_SEND,
    extras={
        droid.Intent.EXTRA_TEXT: "Hello from QPython!",
        droid.Intent.EXTRA_SUBJECT: "Test"
    },
    type="text/plain"
).result
droid.startActivityIntent(intent)
```

### Open File

```python
intent = droid.makeIntent(
    action=droid.Intent.ACTION_VIEW,
    uri="file:///sdcard/document.pdf",
    type="application/pdf"
).result
droid.startActivityIntent(intent)
```

### Pick Contact

```python
result = droid.pickContact()
contact_uri = result.result
```

### Send Email

```python
intent = droid.makeIntent(
    action=droid.Intent.ACTION_SEND,
    extras={
        droid.Intent.EXTRA_EMAIL: ["test@example.com"],
        droid.Intent.EXTRA_SUBJECT: "Hello",
        droid.Intent.EXTRA_TEXT: "Message body"
    },
    type="message/rfc822"
).result
droid.startActivityIntent(intent)
```

### Open App

```python
intent = droid.makeIntent(
    action=droid.Intent.ACTION_MAIN,
    packagename="com.android.settings",
    classname="com.android.settings.Settings"
).result
droid.startActivityIntent(intent)
```
