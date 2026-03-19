# Activity Result API

Set activity results for scripts launched via `startActivityForResult`.

## Result Methods

### setResultBoolean() *ASL4A*
Set a boolean result.

```python
setResultBoolean(resultCode, resultValue)
```

**Parameters:**
- `resultCode` (int): Result code
- `resultValue` (bool): Boolean result value

### setResultByte() *ASL4A*
Set a byte result.

```python
setResultByte(resultCode, resultValue)
```

**Parameters:**
- `resultCode` (int): Result code
- `resultValue` (int): Byte result value

### setResultShort() *ASL4A*
Set a short result.

```python
setResultShort(resultCode, resultValue)
```

**Parameters:**
- `resultCode` (int): Result code
- `resultValue` (int): Short result value

### setResultChar() *ASL4A*
Set a character result.

```python
setResultChar(resultCode, resultValue)
```

**Parameters:**
- `resultCode` (int): Result code
- `resultValue` (str): Character result value

### setResultInteger() *ASL4A*
Set an integer result.

```python
setResultInteger(resultCode, resultValue)
```

**Parameters:**
- `resultCode` (int): Result code
- `resultValue` (int): Integer result value

### setResultLong() *ASL4A*
Set a long result.

```python
setResultLong(resultCode, resultValue)
```

**Parameters:**
- `resultCode` (int): Result code
- `resultValue` (int): Long result value

### setResultFloat() *ASL4A*
Set a float result.

```python
setResultFloat(resultCode, resultValue)
```

**Parameters:**
- `resultCode` (int): Result code
- `resultValue` (float): Float result value

### setResultDouble() *ASL4A*
Set a double result.

```python
setResultDouble(resultCode, resultValue)
```

**Parameters:**
- `resultCode` (int): Result code
- `resultValue` (float): Double result value

### setResultString() *ASL4A*
Set a string result.

```python
setResultString(resultCode, resultValue)
```

**Parameters:**
- `resultCode` (int): Result code
- `resultValue` (str): String result value

### setResultBooleanArray() *ASL4A*
Set a boolean array result.

```python
setResultBooleanArray(resultCode, resultValue)
```

**Parameters:**
- `resultCode` (int): Result code
- `resultValue` (list): Boolean array

### setResultByteArray() *ASL4A*
Set a byte array result.

```python
setResultByteArray(resultCode, resultValue)
```

**Parameters:**
- `resultCode` (int): Result code
- `resultValue` (list): Byte array

### setResultShortArray() *ASL4A*
Set a short array result.

```python
setResultShortArray(resultCode, resultValue)
```

**Parameters:**
- `resultCode` (int): Result code
- `resultValue` (list): Short array

### setResultCharArray() *ASL4A*
Set a character array result.

```python
setResultCharArray(resultCode, resultValue)
```

**Parameters:**
- `resultCode` (int): Result code
- `resultValue` (list): Char array

### setResultIntegerArray() *ASL4A*
Set an integer array result.

```python
setResultIntegerArray(resultCode, resultValue)
```

**Parameters:**
- `resultCode` (int): Result code
- `resultValue` (list): Integer array

### setResultLongArray() *ASL4A*
Set a long array result.

```python
setResultLongArray(resultCode, resultValue)
```

**Parameters:**
- `resultCode` (int): Result code
- `resultValue` (list): Long array

### setResultFloatArray() *ASL4A*
Set a float array result.

```python
setResultFloatArray(resultCode, resultValue)
```

**Parameters:**
- `resultCode` (int): Result code
- `resultValue` (list): Float array

### setResultDoubleArray() *ASL4A*
Set a double array result.

```python
setResultDoubleArray(resultCode, resultValue)
```

**Parameters:**
- `resultCode` (int): Result code
- `resultValue` (list): Double array

### setResultStringArray() *ASL4A*
Set a string array result.

```python
setResultStringArray(resultCode, resultValue)
```

**Parameters:**
- `resultCode` (int): Result code
- `resultValue` (list): String array

### setResultSerializable() *ASL4A*
Set a serializable result.

```python
setResultSerializable(resultCode, resultValue)
```

**Parameters:**
- `resultCode` (int): Result code
- `resultValue`: Serializable result value

## Usage Example

```python
import androidhelper

droid = androidhelper.Android()

# After performing an activity, set the result
# Example: Return success with data
droid.setResultInteger(0, 200)  # RESULT_OK
droid.setResultString(0, "Operation completed successfully")

# Return an array result
droid.setResultIntegerArray(0, [1, 2, 3, 4, 5])
```
