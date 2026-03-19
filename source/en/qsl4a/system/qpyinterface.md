# QPython Interface API

Execute QPython scripts and manage shared variables from other apps.

## Script Execution Methods

### executeQPy() *ASL4A*
Execute a QPython script.

```python
executeQPy(path="", arg=None)
```

**Parameters:**
- `path` (str): Path to the script file
- `arg` (str, optional): Command line arguments

**Returns:** True if started successfully

### executeQPyAsSrv() *ASL4A*
Execute a QPython script as a service.

```python
executeQPyAsSrv(path=None)
```

**Parameters:**
- `path` (str, optional): Path to the script file

**Returns:** True if started successfully

### executeQPyCode() *ASL4A*
Execute Python code directly.

```python
executeQPyCode(code=None)
```

**Parameters:**
- `code` (str, optional): Python code to execute

**Returns:** True if started successfully

### executeQPyCodeAsSrv() *ASL4A*
Execute Python code as a service.

```python
executeQPyCodeAsSrv(code=None)
```

**Parameters:**
- `code` (str, optional): Python code to execute

**Returns:** True if started successfully

## Shared Variables

Shared variables allow communication between QPython and other apps.

### sharedVariableSet() *ASL4A*
Set a Java shared variable.

```python
sharedVariableSet(key, value)
```

**Parameters:**
- `key` (str): Variable name
- `value` (str): Variable value

**Returns:** The stored value

### sharedVariableGet() *ASL4A*
Get a Java shared variable.

```python
sharedVariableGet(key)
```

**Parameters:**
- `key` (str): Variable name

**Returns:** The stored value

### sharedVariableRemove() *ASL4A*
Remove a Java shared variable.

```python
sharedVariableRemove(key)
```

**Parameters:**
- `key` (str): Variable name to remove

**Returns:** The removed value

### getLastLog() *ASL4A*
Get the last log output from QPython.

```python
getLastLog()
```

**Returns:** String log content

## Usage Example

```python
import androidhelper

droid = androidhelper.Android()

# Execute a script
droid.executeQPy("/sdcard/my_script.py", arg="test")

# Execute code directly
code = "print('Hello from QPython!')"
droid.executeQPyCode(code)

# Use shared variables
droid.sharedVariableSet("username", "alice")
username = droid.sharedVariableGet("username").result
print(f"Username: {username}")

# Remove variable
droid.sharedVariableRemove("username")

# Get recent log
log = droid.getLastLog().result
print(f"Log: {log}")
```
