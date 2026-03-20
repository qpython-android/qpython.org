# Intent 系统

Android Intent 用于启动活动、发送广播和应用间通信。QSL4A 通过 `Intent` 模块提供完整的 Intent 支持。

## 模块导入

```python
import androidhelper
don = androidhelper.Android()
```

## Intent 常量

通过 `droid.Intent` 访问：

### 操作

| 常量 | 值 | 用途 |
|----------|-------|-------|
| `ACTION_MAIN` | android.intent.action.MAIN | 应用入口点 |
| `ACTION_VIEW` | android.intent.action.VIEW | 查看内容 |
| `ACTION_EDIT` | android.intent.action.EDIT | 编辑内容 |
| `ACTION_PICK` | android.intent.action.PICK | 选择项目 |
| `ACTION_SEND` | android.intent.action.SEND | 分享内容 |
| `ACTION_SEARCH` | android.intent.action.SEARCH | 搜索 |

### 标志

| 常量 | 值 | 用途 |
|----------|-------|-------|
| `FLAG_ACTIVITY_NEW_TASK` | 268435456 | 启动新任务 |
| `FLAG_ACTIVITY_CLEAR_TASK` | 32768 | 清除任务堆栈 |
| `FLAG_ACTIVITY_NEW_DOCUMENT` | 524288 | 新文档模式 |

### 附加数据

| 常量 | 用途 |
|----------|-------|
| `EXTRA_TEXT` | 文本内容 |
| `EXTRA_STREAM` | 文件 URI |
| `EXTRA_SUBJECT` | 主题行 |
| `EXTRA_EMAIL` | 电子邮件地址 |

## 核心方法

### makeIntent()
创建 Intent 对象。

```python
makeIntent(action, uri=None, type=None, extras=None, categories=None,
           packagename=None, classname=None, flags=None)
```

**参数：**
- `action` (str): Intent 操作（例如 `droid.Intent.ACTION_VIEW`）
- `uri` (str, optional): 数据 URI
- `type` (str, optional): MIME 类型
- `extras` (dict, optional): 附加数据
- `categories` (list, optional): Intent 类别
- `packagename` (str, optional): 目标包
- `classname` (str, optional): 目标类
- `flags` (int, optional): Intent 标志

**返回：** Intent 对象

### startActivityIntent()
使用 Intent 启动 Activity。

```python
startActivityIntent(intent, wait=None)
```

**参数：**
- `intent`: makeIntent() 返回的 Intent 对象
- `wait` (bool, optional): 阻塞直到活动关闭

### startActivityForResultIntent()
启动活动并等待结果。

```python
startActivityForResultIntent(intent)
```

**返回：** Activity 结果

### sendBroadcastIntent()
发送广播。

```python
sendBroadcastIntent(intent)
```

### view()
通过 URI 查看内容。

```python
view(uri, type=None, extras=None)
```

### pick()
从 URI 选择内容。

```python
pick(uri)
```

## 常见 Intent 方法 *ASL4A*

### scanBarcode() *ASL4A*
启动条码扫描器。

```python
scanBarcode()
```

**返回：** 扫描的条码字符串

### send() *ASL4A*
通过分享 Intent 发送内容。

```python
send(type, content)
```

**参数：**
- `type` (str): MIME 类型
- `content` (str): 要分享的内容

### sendText() *ASL4A*
发送文本内容。

```python
sendText(text)
```

**参数：**
- `text` (str): 要发送的文本

### sendEmail() *ASL4A*
发送电子邮件。

```python
sendEmail(to, subject, body, attachment=None)
```

**参数：**
- `to` (str or list): 收件人电子邮件地址
- `subject` (str): 电子邮件主题
- `body` (str): 电子邮件正文
- `attachment` (str, optional): 附件文件路径

### pathToUri() *ASL4A*
将文件路径转换为内容 URI。

```python
pathToUri(path)
```

**参数：**
- `path` (str): 文件路径

**返回：** 内容 URI 字符串

### openFile() *ASL4A*
用适当的应用程序打开文件。

```python
openFile(path)
```

**参数：**
- `path` (str): 要打开的文件路径

### sendFile() *ASL4A*
通过分享 Intent 发送文件。

```python
sendFile(path)
```

**参数：**
- `path` (str): 要发送的文件路径

### getPathType() *ASL4A*
获取文件路径的 MIME 类型。

```python
getPathType(path)
```

**参数：**
- `path` (str): 文件路径

**返回：** MIME 类型字符串

### viewMap() *ASL4A*
在指定位置打开地图。

```python
viewMap(latitude, longitude)
```

**参数：**
- `latitude` (float): 纬度
- `longitude` (float): 经度

### viewContacts() *ASL4A*
打开联系人应用。

```python
viewContacts()
```

### search() *ASL4A*
执行网络搜索。

```python
search(query)
```

**参数：**
- `query` (str): 搜索查询

### viewHtml() *ASL4A*
查看 HTML 内容。

```python
viewHtml(content, encoding=None)
```

**参数：**
- `content` (str): HTML 内容
- `encoding` (str, optional): 字符编码

### webViewShow() *ASL4A*
在 WebView 中显示网页内容。已废弃，请使用 viewHtml。

```python
webViewShow(url)
```

**参数：**
- `url` (str): 网页 URL

### editorOpen() *ASL4A*
打开文本编辑器。

```python
editorOpen(path=None, create=False)
```

**参数：**
- `path` (str, optional): 要编辑的文件路径
- `create` (bool, optional): 如果不存在则创建

## 辅助类：Uri

创建 Intent 的 URI 对象：

```python
from androidhelper.Intent import Uri

uri = Uri("file:///sdcard/test.txt")
```

## 使用示例

### 打开网页

```python
intent = droid.makeIntent(
    action=droid.Intent.ACTION_VIEW,
    uri="http://www.example.com"
).result
droid.startActivityIntent(intent)
```

### 分享文本

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

### 打开文件

```python
intent = droid.makeIntent(
    action=droid.Intent.ACTION_VIEW,
    uri="file:///sdcard/document.pdf",
    type="application/pdf"
).result
droid.startActivityIntent(intent)
```

### 选择联系人

```python
result = droid.pickContact()
contact_uri = result.result
```

### 发送电子邮件

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

### 打开应用

```python
intent = droid.makeIntent(
    action=droid.Intent.ACTION_MAIN,
    packagename="com.android.settings",
    classname="com.android.settings.Settings"
).result
droid.startActivityIntent(intent)
```
