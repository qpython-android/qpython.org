# Android Base Class

The `Android` class is the core of QSL4A, providing the connection to the Android runtime and RPC mechanism.

## Module Import

```python
# Full featured (recommended)
import androidhelper
droid = androidhelper.Android()

# Minimal version (quick, single instance)
import android
droid = android.droid
```

## Class: Android

### Constructor

```python
Android(addr=None)
```

**Parameters:**
- `addr` (tuple, optional): (HOST, PORT) address. If None, uses environment variables `AP_HOST` and `AP_PORT`

**Environment Variables:**
- `AP_HOST` - Server host address
- `AP_PORT` - Server port
- `AP_HANDSHAKE` - Authentication token

### Core Methods

#### _rpc()
Internal RPC method for calling Android functions.

```python
_rpc(method, *args)
```

**Parameters:**
- `method` (str): Method name to call
- `*args`: Variable arguments for the method

**Returns:** `Result` namedtuple with fields:
- `id` (int): Request ID
- `result`: Method return value
- `error` (str or None): Error message if failed

#### __getattr__()
Dynamic method dispatcher. All Android methods are accessed via attribute lookup.

```python
# These are equivalent:
droid.makeToast("Hello")
droid._rpc("makeToast", "Hello")
```

## Standalone Functions (android.py)

When using the minimal `android` module:

### jsla()
Send JSON-RPC request and return raw response.

```python
jsla(method, *params)
```

**Returns:** JSON string response

### rsla()
Send request and return result only.

```python
rsla(method, *params)
```

**Returns:** Result value from RPC call

### esla()
Send request, raise exception on error.

```python
esla(method, *params)
```

**Raises:** Exception if error field is not None

### nsla()
Send request and return Result namedtuple.

```python
nsla(method, *params)
```

**Returns:** Result namedtuple

## Usage Examples

### Basic Connection

```python
import androidhelper

# Connect to Android runtime
droid = androidhelper.Android()

# Check connection by showing toast
droid.makeToast("Connected!")
```

### Error Handling

```python
result = droid.someMethod()
if result.error:
    print(f"Error: {result.error}")
else:
    print(f"Success: {result.result}")
```

### Direct RPC Call

```python
# Call any method directly
result = droid._rpc("makeToast", "Hello World")
```
