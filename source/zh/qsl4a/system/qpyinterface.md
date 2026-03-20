# QPython 接口 API

从其他应用执行 QPython 脚本和管理共享变量。

## 脚本执行方法

### executeQPy()
执行 QPython 脚本。

```python
executeQPy(path="", arg=None)
```

**参数：**
- `path` (str): 脚本文件路径
- `arg` (str, optional): 命令行参数

**返回：** 如果启动成功则为 True

### executeQPyAsSrv()
作为服务执行 QPython 脚本。

```python
executeQPyAsSrv(path=None)
```

**参数：**
- `path` (str, optional): 脚本文件路径

**返回：** 如果启动成功则为 True

### executeQPyCode()
直接执行 Python 代码。

```python
executeQPyCode(code=None)
```

**参数：**
- `code` (str, optional): 要执行的 Python 代码

**返回：** 如果启动成功则为 True

### executeQPyCodeAsSrv()
作为服务执行 Python 代码。

```python
executeQPyCodeAsSrv(code=None)
```

**参数：**
- `code` (str, optional): 要执行的 Python 代码

**返回：** 如果启动成功则为 True

## 共享变量

共享变量允许 QPython 与其他应用之间进行通信。

### sharedVariableSet()
设置 Java 共享变量。

```python
sharedVariableSet(key, value)
```

**参数：**
- `key` (str): 变量名
- `value` (str): 变量值

**返回：** 存储的值

### sharedVariableGet()
获取 Java 共享变量。

```python
sharedVariableGet(key)
```

**参数：**
- `key` (str): 变量名

**返回：** 存储的值

### sharedVariableRemove()
移除 Java 共享变量。

```python
sharedVariableRemove(key)
```

**参数：**
- `key` (str): 要移除的变量名

**返回：** 被移除的值

### getLastLog()
获取 QPython 的最后日志输出。

```python
getLastLog()
```

**返回：** 字符串日志内容

## 使用示例

```python
import androidhelper

droid = androidhelper.Android()

# 执行脚本
droid.executeQPy("/sdcard/my_script.py", arg="test")

# 直接执行代码
code = "print('Hello from QPython!')"
droid.executeQPyCode(code)

# 使用共享变量
droid.sharedVariableSet("username", "alice")
username = droid.sharedVariableGet("username").result
print(f"Username: {username}")

# 移除变量
droid.sharedVariableRemove("username")

# 获取最近日志
log = droid.getLastLog().result
print(f"Log: {log}")
```
