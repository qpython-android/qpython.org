# Android 基础类

`Android` 类是 QSL4A 的核心，提供了与 Android 运行时的连接和 RPC 机制。

## 模块导入

```python
# 功能完整版本（推荐）
import androidhelper
droid = androidhelper.Android()

# 简化版本（快速，单实例）
import android
droid = android.droid
```

## 类：Android

### 构造函数

```python
Android(addr=None)
```

**参数：**
- `addr` (tuple, optional): (HOST, PORT) 地址。如果为 None，则使用环境变量 `AP_HOST` 和 `AP_PORT`

**环境变量：**
- `AP_HOST` - 服务器主机地址
- `AP_PORT` - 服务器端口
- `AP_HANDSHAKE` - 认证令牌

### 核心方法

#### _rpc()
调用 Android 函数的内部 RPC 方法。

```python
_rpc(method, *args)
```

**参数：**
- `method` (str): 要调用的方法名
- `*args`: 方法的可变参数

**返回：** `Result` 命名元组，包含以下字段：
- `id` (int): 请求 ID
- `result`: 方法返回值
- `error` (str or None): 错误信息（如果失败）

#### __getattr__()
动态方法分发器。所有 Android 方法都通过属性查找访问。

```python
# 以下两种方式等价：
droid.makeToast("Hello")
droid._rpc("makeToast", "Hello")
```

## 独立函数（android.py）

使用简化的 `android` 模块时：

### jsla()
发送 JSON-RPC 请求并返回原始响应。

```python
jsla(method, *params)
```

**返回：** JSON 字符串响应

### rsla()
发送请求并仅返回结果。

```python
rsla(method, *params)
```

**返回：** RPC 调用的结果值

### esla()
发送请求，错误时抛出异常。

```python
esla(method, *params)
```

**抛出：** 如果 error 字段不为 None 则抛出异常

### nsla()
发送请求并返回 Result 命名元组。

```python
nsla(method, *params)
```

**返回：** Result 命名元组

## 使用示例

### 基本连接

```python
import androidhelper

# 连接到 Android 运行时
droid = androidhelper.Android()

# 通过显示 toast 来检查连接
droid.makeToast("Connected!")
```

### 错误处理

```python
result = droid.someMethod()
if result.error:
    print(f"Error: {result.error}")
else:
    print(f"Success: {result.result}")
```

### 直接 RPC 调用

```python
# 直接调用任意方法
result = droid._rpc("makeToast", "Hello World")
```
