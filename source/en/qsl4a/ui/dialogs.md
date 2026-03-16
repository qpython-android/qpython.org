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

### dialogShowSimpleChoice()
Show a simple choice dialog with items.

```python
dialogShowSimpleChoice(title="Alert", message="The message of the alert.",
                       items=None, positiveButtonText="OK",
                       negativeButtonText=None, neutralButtonText=None,
                       messageIsHtml=False)
```

**Parameters:**
- `items` (list): List of choice strings

**Returns:** Result with selected item

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

**Returns:** Result with password entered

### dialogCreateInput()
Create a custom input dialog.

```python
dialogCreateInput(title="Value", message="Please enter value:",
                  defaultText=None, inputType=None)
```

**Parameters:**
- `inputType` (str): Input type (e.g., "text", "number", "textPassword")

### dialogCreatePassword()
Create a password input dialog.

```python
dialogCreatePassword(title="Password", message="Please enter password:")
```

### dialogCreateSeekBar()
Create a seek bar/slider dialog.

```python
dialogCreateSeekBar(starting_value=50, maximum_value=100, title="", message="")
```

**Parameters:**
- `starting_value` (int): Initial value
- `maximum_value` (int): Maximum value

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

**Parameters:**
- `items` (list): List of choice strings
- `selected` (list): List of initially selected indices

### dialogSetSingleChoiceItems()
Set single choice items for a dialog.

```python
dialogSetSingleChoiceItems(items, selected=-1)
```

### dialogSetMultiChoiceItems()
Set multiple choice items for a dialog.

```python
dialogSetMultiChoiceItems(items, selected=None)
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

### dialogSetMaxProgress()
Set maximum progress value.

```python
dialogSetMaxProgress(max)
```

### dialogSetProgressMessage()
Update the progress dialog message.

```python
dialogSetProgressMessage(message)
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

## Custom Dialog Creation

### dialogCreateAlert()
Create a custom alert dialog.

```python
dialogCreateAlert(title=None, message=None)
```

Creates an empty alert dialog. Use with other dialogSet* functions to customize.

### dialogSetItems()
Set simple list items for the dialog.

```python
dialogSetItems(items)
```

### dialogSetPositiveButtonText()
Set positive button text.

```python
dialogSetPositiveButtonText(text)
```

### dialogSetNegativeButtonText()
Set negative button text.

```python
dialogSetNegativeButtonText(text)
```

### dialogSetNeutralButtonText()
Set neutral button text.

```python
dialogSetNeutralButtonText(text)
```

### dialogSetMessageIsHtml()
Set whether message should be parsed as HTML.

```python
dialogSetMessageIsHtml(messageIsHtml=True)
```

### dialogShow()
Show the created custom dialog.

```python
dialogShow()
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

## Usage Examples

### Simple Alert

```python
import androidhelper

droid = androidhelper.Android()

# Show alert
droid.dialogShowAlert("Warning", "This is an important message!")
```

### Input Dialog

```python
# Get user input
result = droid.dialogGetInput("Name", "Enter your name:", "John").result
print(f"Hello, {result}!")
```

### Custom Dialog with Buttons

```python
# Create custom dialog
droid.dialogCreateAlert("Custom", "Choose an option")
droid.dialogSetItems(["Option 1", "Option 2", "Option 3"])
droid.dialogShow()

# Get response
response = droid.dialogGetResponse().result
print(f"Selected: {response['item']}")
```

### Progress Dialog

```python
# Create progress dialog
droid.dialogCreateHorizontalProgress("Loading", "Please wait...", 100)
droid.dialogShow()

# Update progress
for i in range(101):
    droid.dialogSetCurrentProgress(i)
    time.sleep(0.05)

droid.dialogDismiss()
```

### Date Picker

```python
# Show date picker
droid.dialogCreateDatePicker(2024, 1, 15)
droid.dialogShow()
response = droid.dialogGetResponse().result
print(f"Selected: {response}")
```
