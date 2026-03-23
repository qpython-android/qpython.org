# 密码 API

用于安全数据存储的加密和解密工具。

## 初始化

### cipherInit()
使用加密密钥和算法初始化密码器。

```python
cipherInit(key, algorithm="AES/CBC/PKCS5Padding", encodingFormat="", initialVector="")
```

**参数：**
- `key` (str or bytes): 加密密钥
- `algorithm` (str): 密码算法（默认："AES/CBC/PKCS5Padding"）
- `encodingFormat` (str): 编码格式
- `initialVector` (str or bytes): 加密的初始向量

**返回：** 初始化结果

**注意：** 必须在任何加密/解密操作之前调用。

## 加密方法

### encryptString()
加密字符串。

```python
encryptString(plainText)
```

**参数：**
- `plainText` (str): 要加密的文本

**返回：** 加密的字符串

### encryptBytes()
加密字节数据。

```python
encryptBytes(data)
```

**参数：**
- `data` (bytes): 要加密的数据

**返回：** 加密的字节

### encryptStringToFile()
加密字符串到文件。

```python
encryptStringToFile(plainText, filePath)
```

**参数：**
- `plainText` (str): 要加密的文本
- `filePath` (str): 输出文件路径

### encryptBytesToFile()
加密字节到文件。

```python
encryptBytesToFile(data, filePath)
```

## 解密方法

### decryptString()
解密为字符串。

```python
decryptString(cipherText)
```

**参数：**
- `cipherText` (str): 加密的文本

**返回：** 解密的字符串

### decryptBytes()
解密为字节。

```python
decryptBytes(data)
```

**返回：** 解密的字节

### decryptFileToString()
解密文件到字符串。

```python
decryptFileToString(filePath)
```

### decryptFileToBytes()
解密文件到字节。

```python
decryptFileToBytes(filePath)
```

### decryptFile()
解密文件到文件。

```python
decryptFile(srcPath, destPath)
```

## 使用示例

```python
import androidhelper

droid = androidhelper.Android()

# 使用加密密钥初始化密码器
droid.cipherInit("my_secret_key_1234")

# 加密字符串
encrypted = droid.encryptString("Secret message!").result
print(f"Encrypted: {encrypted}")

# 解密字符串
decrypted = droid.decryptString(encrypted).result
print(f"Decrypted: {decrypted}")

# 加密到文件
droid.encryptStringToFile("My secret data", "/sdcard/secret.dat")

# 从文件解密
data = droid.decryptFileToString("/sdcard/secret.dat").result
print(data)

# 使用自定义算法和 IV 初始化
droid.cipherInit(
    key="my_key",
    algorithm="AES/CBC/PKCS5Padding",
    initialVector="0123456789abcdef"
)
```
