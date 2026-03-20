# Activity Result API

为通过 `startActivityForResult` 启动的脚本设置 activity 结果。

## 结果方法

### setResultBoolean() *ASL4A*
设置布尔结果。

```python
setResultBoolean(resultCode, resultValue)
```

**参数：**
- `resultCode` (int): 结果代码
- `resultValue` (bool): 布尔结果值

### setResultByte() *ASL4A*
设置字节结果。

```python
setResultByte(resultCode, resultValue)
```

**参数：**
- `resultCode` (int): 结果代码
- `resultValue` (int): 字节结果值

### setResultShort() *ASL4A*
设置短整数结果。

```python
setResultShort(resultCode, resultValue)
```

**参数：**
- `resultCode` (int): 结果代码
- `resultValue` (int): 短整数结果值

### setResultChar() *ASL4A*
设置字符结果。

```python
setResultChar(resultCode, resultValue)
```

**参数：**
- `resultCode` (int): 结果代码
- `resultValue` (str): 字符结果值

### setResultInteger() *ASL4A*
设置整数结果。

```python
setResultInteger(resultCode, resultValue)
```

**参数：**
- `resultCode` (int): 结果代码
- `resultValue` (int): 整数结果值

### setResultLong() *ASL4A*
设置长整数结果。

```python
setResultLong(resultCode, resultValue)
```

**参数：**
- `resultCode` (int): 结果代码
- `resultValue` (int): 长整数结果值

### setResultFloat() *ASL4A*
设置浮点数结果。

```python
setResultFloat(resultCode, resultValue)
```

**参数：**
- `resultCode` (int): 结果代码
- `resultValue` (float): 浮点数结果值

### setResultDouble() *ASL4A*
设置双精度浮点数结果。

```python
setResultDouble(resultCode, resultValue)
```

**参数：**
- `resultCode` (int): 结果代码
- `resultValue` (float): 双精度浮点数结果值

### setResultString() *ASL4A*
设置字符串结果。

```python
setResultString(resultCode, resultValue)
```

**参数：**
- `resultCode` (int): 结果代码
- `resultValue` (str): 字符串结果值

### setResultBooleanArray() *ASL4A*
设置布尔数组结果。

```python
setResultBooleanArray(resultCode, resultValue)
```

**参数：**
- `resultCode` (int): 结果代码
- `resultValue` (list): 布尔数组

### setResultByteArray() *ASL4A*
设置字节数组结果。

```python
setResultByteArray(resultCode, resultValue)
```

**参数：**
- `resultCode` (int): 结果代码
- `resultValue` (list): 字节数组

### setResultShortArray() *ASL4A*
设置短整数数组结果。

```python
setResultShortArray(resultCode, resultValue)
```

**参数：**
- `resultCode` (int): 结果代码
- `resultValue` (list): 短整数数组

### setResultCharArray() *ASL4A*
设置字符数组结果。

```python
setResultCharArray(resultCode, resultValue)
```

**参数：**
- `resultCode` (int): 结果代码
- `resultValue` (list): 字符数组

### setResultIntegerArray() *ASL4A*
设置整数数组结果。

```python
setResultIntegerArray(resultCode, resultValue)
```

**参数：**
- `resultCode` (int): 结果代码
- `resultValue` (list): 整数数组

### setResultLongArray() *ASL4A*
设置长整数数组结果。

```python
setResultLongArray(resultCode, resultValue)
```

**参数：**
- `resultCode` (int): 结果代码
- `resultValue` (list): 长整数数组

### setResultFloatArray() *ASL4A*
设置浮点数数组结果。

```python
setResultFloatArray(resultCode, resultValue)
```

**参数：**
- `resultCode` (int): 结果代码
- `resultValue` (list): 浮点数数组

### setResultDoubleArray() *ASL4A*
设置双精度浮点数数组结果。

```python
setResultDoubleArray(resultCode, resultValue)
```

**参数：**
- `resultCode` (int): 结果代码
- `resultValue` (list): 双精度浮点数数组

### setResultStringArray() *ASL4A*
设置字符串数组结果。

```python
setResultStringArray(resultCode, resultValue)
```

**参数：**
- `resultCode` (int): 结果代码
- `resultValue` (list): 字符串数组

### setResultSerializable() *ASL4A*
设置可序列化结果。

```python
setResultSerializable(resultCode, resultValue)
```

**参数：**
- `resultCode` (int): 结果代码
- `resultValue`: 可序列化结果值

## 使用示例

```python
import androidhelper

droid = androidhelper.Android()

# 执行 activity 后，设置结果
# 示例：返回成功及数据
droid.setResultInteger(0, 200)  # RESULT_OK
droid.setResultString(0, "Operation completed successfully")

# 返回数组结果
droid.setResultIntegerArray(0, [1, 2, 3, 4, 5])
```
