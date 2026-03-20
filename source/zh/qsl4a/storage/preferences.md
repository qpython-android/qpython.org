# 偏好设置 API

使用 Android SharedPreferences 存储和检索数据。

## 偏好设置方法

### prefGetValue()
从共享偏好设置读取值。

```python
prefGetValue(key, filename=None)
```

**参数：**
- `key` (str): 偏好设置键
- `filename` (str, optional): 偏好设置文件名

**返回：** 存储的值（任意类型）

### prefPutValue()
写入值到共享偏好设置。

```python
prefPutValue(key, value, filename=None)
```

**参数：**
- `key` (str): 偏好设置键
- `value` (object): 要存储的值
- `filename` (str, optional): 偏好设置文件名

### prefGetAll()
获取所有偏好设置值。

```python
prefGetAll(filename=None)
```

**参数：**
- `filename` (str, optional): 偏好设置文件名

**返回：** 所有偏好的映射

### prefRemoveValue()
从共享偏好设置中移除值。

```python
prefRemoveValue(key, filename=None)
```

**参数：**
- `key` (str): 要移除的偏好设置键
- `filename` (str, optional): 偏好设置文件名

## 使用示例

```python
import androidhelper

droid = androidhelper.Android()

# 存储值
droid.prefPutValue("username", "alice")
droid.prefPutValue("score", 100)
droid.prefPutValue("enabled", True)

# 读取特定值
username = droid.prefGetValue("username").result
print(f"Username: {username}")

# 获取所有偏好设置
all_prefs = droid.prefGetAll().result
print(f"All prefs: {all_prefs}")

# 移除值
droid.prefRemoveValue("score")

# 使用自定义文件名
droid.prefPutValue("token", "abc123", filename="auth.prefs")
token = droid.prefGetValue("token", filename="auth.prefs").result
```
