# 对话框系统

QSL4A 提供全面的对话框支持，用于用户交互，包括警报、输入对话框、选择对话框和进度对话框。

## 警报对话框

### dialogShowAlert()
显示简单警报对话框。

```python
dialogShowAlert(title="Alert", message="The message of the alert.",
                positiveButtonText="OK", negativeButtonText=None,
                neutralButtonText=None, messageIsHtml=False)
```

**参数：**
- `title` (str): 对话框标题
- `message` (str): 消息文本
- `positiveButtonText` (str): 肯定按钮标签
- `negativeButtonText` (str, optional): 否定按钮标签
- `neutralButtonText` (str, optional): 中性按钮标签
- `messageIsHtml` (bool): 将消息解析为 HTML

**返回：** 包含点击按钮的结果

### dialogShowSimpleChoice()
显示带有项目的简单选择对话框。

```python
dialogShowSimpleChoice(title="Alert", message="The message of the alert.",
                       items=None, positiveButtonText="OK",
                       negativeButtonText=None, neutralButtonText=None,
                       messageIsHtml=False)
```

**参数：**
- `items` (list): 选择字符串列表

**返回：** 包含选中项目的结果

## 输入对话框

### dialogGetInput()
获取用户文本输入。

```python
dialogGetInput(title="Value", message="Please enter value:",
               defaultText=None, messageIsHtml=False)
```

**返回：** 包含用户输入文本的结果

### dialogGetPassword()
获取密码输入。

```python
dialogGetPassword(title="Password", message="Please enter password:")
```

**返回：** 包含输入密码的结果

### dialogCreateInput()
创建自定义输入对话框。

```python
dialogCreateInput(title="Value", message="Please enter value:",
                  defaultText=None, inputType=None)
```

**参数：**
- `inputType` (str): 输入类型（例如 "text"、"number"、"textPassword"）

### dialogCreatePassword()
创建密码输入对话框。

```python
dialogCreatePassword(title="Password", message="Please enter password:")
```

### dialogCreateSeekBar()
创建滑块/进度条对话框。

```python
dialogCreateSeekBar(starting_value=50, maximum_value=100, title="", message="")
```

**参数：**
- `starting_value` (int): 初始值
- `maximum_value` (int): 最大值

## 选择对话框

### dialogShowSingleChoice()
显示单选（单选按钮）对话框。

```python
dialogShowSingleChoice(title="Alert", message="The message of the alert.",
                       items=None, selected=-1, positiveButtonText="OK",
                       negativeButtonText=None, neutralButtonText=None,
                       messageIsHtml=False)
```

**参数：**
- `items` (list): 选择字符串列表
- `selected` (int): 默认选中索引

### dialogShowMultiChoice()
显示多选（复选框）对话框。

```python
dialogShowMultiChoice(title="Alert", message="The message of the alert.",
                      items=None, selected=None, positiveButtonText="OK",
                      negativeButtonText=None, neutralButtonText=None,
                      messageIsHtml=False)
```

**参数：**
- `items` (list): 选择字符串列表
- `selected` (list): 初始选中索引列表

### dialogSetSingleChoiceItems()
为对话框设置单选项目。

```python
dialogSetSingleChoiceItems(items, selected=-1)
```

### dialogSetMultiChoiceItems()
为对话框设置多选项目。

```python
dialogSetMultiChoiceItems(items, selected=None)
```

## 进度对话框

### dialogCreateSpinnerProgress()
创建不确定进度对话框。

```python
dialogCreateSpinnerProgress(title=None, message=None, maximum_progress=100)
```

### dialogCreateHorizontalProgress()
创建水平进度对话框。

```python
dialogCreateHorizontalProgress(title=None, message=None, maximum_progress=100)
```

### dialogSetCurrentProgress()
更新进度值。

```python
dialogSetCurrentProgress(current)
```

### dialogSetMaxProgress()
设置最大进度值。

```python
dialogSetMaxProgress(max)
```

### dialogSetProgressMessage()
更新进度对话框消息。

```python
dialogSetProgressMessage(message)
```

## 选择器对话框

### dialogCreateDatePicker()
创建日期选择器对话框。

```python
dialogCreateDatePicker(year=1970, month=1, day=1)
```

### dialogCreateTimePicker()
创建时间选择器对话框。

```python
dialogCreateTimePicker(hour=0, minute=0, is24hour=False)
```

## 自定义对话框创建

### dialogCreateAlert()
创建自定义警报对话框。

```python
dialogCreateAlert(title=None, message=None)
```

创建一个空警报对话框。可与其他 dialogSet* 函数一起使用来自定义。

### dialogSetItems()
为对话框设置简单列表项目。

```python
dialogSetItems(items)
```

### dialogSetPositiveButtonText()
设置肯定按钮文本。

```python
dialogSetPositiveButtonText(text)
```

### dialogSetNegativeButtonText()
设置否定按钮文本。

```python
dialogSetNegativeButtonText(text)
```

### dialogSetNeutralButtonText()
设置中性按钮文本。

```python
dialogSetNeutralButtonText(text)
```

### dialogSetMessageIsHtml()
设置消息是否应解析为 HTML。

```python
dialogSetMessageIsHtml(messageIsHtml=True)
```

### dialogShow()
显示创建的自定义对话框。

```python
dialogShow()
```

## 对话框控制

### dialogDismiss()
关闭当前对话框。

```python
dialogDismiss()
```

### dialogGetResponse()
获取对话框响应。

```python
dialogGetResponse()
```

### dialogGetSelectedItems()
从选择对话框获取选中的项目。

```python
dialogGetSelectedItems()
```

## 使用示例

### 简单警报

```python
import androidhelper

droid = androidhelper.Android()

# 显示警报
droid.dialogShowAlert("Warning", "This is an important message!")
```

### 输入对话框

```python
# 获取用户输入
result = droid.dialogGetInput("Name", "Enter your name:", "John").result
print(f"Hello, {result}!")
```

### 带按钮的自定义对话框

```python
# 创建自定义对话框
droid.dialogCreateAlert("Custom", "Choose an option")
droid.dialogSetItems(["Option 1", "Option 2", "Option 3"])
droid.dialogShow()

# 获取响应
response = droid.dialogGetResponse().result
print(f"Selected: {response['item']}")
```

### 进度对话框

```python
# 创建进度对话框
droid.dialogCreateHorizontalProgress("Loading", "Please wait...", 100)
droid.dialogShow()

# 更新进度
for i in range(101):
    droid.dialogSetCurrentProgress(i)
    time.sleep(0.05)

droid.dialogDismiss()
```

### 日期选择器

```python
# 显示日期选择器
droid.dialogCreateDatePicker(2024, 1, 15)
droid.dialogShow()
response = droid.dialogGetResponse().result
print(f"Selected: {response}")
```
