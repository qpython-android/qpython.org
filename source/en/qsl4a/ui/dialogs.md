# Dialog System

QSL4A provides comprehensive dialog support for user interaction, including alerts, input dialogs, choice dialogs, and progress dialogs.

## Alert Dialogs

### dialogShowAlert()
Show a simple alert dialog.

```python
dialogShowAlert(title="Alert", message="The message of the alert.",
                positiveButtonText="OK", negativeButtonText=None,
                neutralButtonText=None, messageIsHtml=False)
```

**Parameters:**
- `title` (str): Dialog title
- `message` (str): Message text
- `positiveButtonText` (str): Positive button label
- `negativeButtonText` (str, optional): Negative button label
- `neutralButtonText` (str, optional): Neutral button label
- `messageIsHtml` (bool): Parse message as HTML

**Returns:** Result with button clicked

## Input Dialogs

### dialogGetInput()
Get text input from user.

```python
dialogGetInput(title="Value", message="Please enter value:",
               defaultText=None, messageIsHtml=False)
```

**Returns:** Result with user's input text

### dialogGetPassword()
Get password input.

```python
dialogGetPassword(title="Password", message="Please enter password:")
```

## Choice Dialogs

### dialogShowSingleChoice()
Show single choice (radio) dialog.

```python
dialogShowSingleChoice(title="Alert", message="The message of the alert.",
                       items=None, selected=-1, positiveButtonText="OK",
                       negativeButtonText=None, neutralButtonText=None,
                       messageIsHtml=False)
```

**Parameters:**
- `items` (list): List of choice strings
- `selected` (int): Default selected index

### dialogShowMultiChoice()
Show multiple choice (checkbox) dialog.

```python
dialogShowMultiChoice(title="Alert", message="The message of the alert.",
                      items=None, selected=None, positiveButtonText="OK",
                      negativeButtonText=None, neutralButtonText=None,
                      messageIsHtml=False)
```

## Progress Dialogs

### dialogCreateSpinnerProgress()
Create indeterminate progress dialog.

```python
dialogCreateSpinnerProgress(title=None, message=None, maximum_progress=100)
```

### dialogCreateHorizontalProgress()
Create horizontal progress dialog.

```python
dialogCreateHorizontalProgress(title=None, message=None, maximum_progress=100)
```

### dialogSetCurrentProgress()
Update progress value.

```python
dialogSetCurrentProgress(current)
```

## Picker Dialogs

### dialogCreateDatePicker()
Create date picker dialog.

```python
dialogCreateDatePicker(year=1970, month=1, day=1)
```

### dialogCreateTimePicker()
Create time picker dialog.

```python
dialogCreateTimePicker(hour=0, minute=0, is24hour=False)
```

## Dialog Control

### dialogDismiss()
Dismiss current dialog.

```python
dialogDismiss()
```

### dialogGetResponse()
Get dialog response.

```python
dialogGetResponse()
```

### dialogGetSelectedItems()
Get selected items from choice dialog.

```python
dialogGetSelectedItems()
```
