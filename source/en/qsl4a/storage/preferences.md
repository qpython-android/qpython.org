# Preferences API

Store and retrieve data using Android SharedPreferences.

## Preference Methods

### prefGetValue() *ASL4A*
Read a value from shared preferences.

```python
prefGetValue(key, filename=None)
```

**Parameters:**
- `key` (str): Preference key
- `filename` (str, optional): Preference file name

**Returns:** The stored value (any type)

### prefPutValue() *ASL4A*
Write a value to shared preferences.

```python
prefPutValue(key, value, filename=None)
```

**Parameters:**
- `key` (str): Preference key
- `value` (object): Value to store
- `filename` (str, optional): Preference file name

### prefGetAll() *ASL4A*
Get all preference values.

```python
prefGetAll(filename=None)
```

**Parameters:**
- `filename` (str, optional): Preference file name

**Returns:** Map of all preferences

### prefRemoveValue() *ASL4A*
Remove a value from shared preferences.

```python
prefRemoveValue(key, filename=None)
```

**Parameters:**
- `key` (str): Preference key to remove
- `filename` (str, optional): Preference file name

## Usage Example

```python
import androidhelper

droid = androidhelper.Android()

# Store values
droid.prefPutValue("username", "alice")
droid.prefPutValue("score", 100)
droid.prefPutValue("enabled", True)

# Read a specific value
username = droid.prefGetValue("username").result
print(f"Username: {username}")

# Get all preferences
all_prefs = droid.prefGetAll().result
print(f"All prefs: {all_prefs}")

# Remove a value
droid.prefRemoveValue("score")

# Use custom filename
droid.prefPutValue("token", "abc123", filename="auth.prefs")
token = droid.prefGetValue("token", filename="auth.prefs").result
```
