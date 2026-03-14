# Cipher API

Encryption and decryption utilities for secure data storage.

## Encryption Methods

### encryptString()
Encrypt a string.

```python
encryptString(plainText)
```

**Parameters:**
- `plainText` (str): Text to encrypt

**Returns:** Encrypted string

### encryptBytes()
Encrypt bytes data.

```python
encryptBytes(data)
```

**Parameters:**
- `data` (bytes): Data to encrypt

**Returns:** Encrypted bytes

### encryptStringToFile()
Encrypt string to file.

```python
encryptStringToFile(plainText, filePath)
```

**Parameters:**
- `plainText` (str): Text to encrypt
- `filePath` (str): Output file path

### encryptBytesToFile()
Encrypt bytes to file.

```python
encryptBytesToFile(data, filePath)
```

## Decryption Methods

### decryptString()
Decrypt to string.

```python
decryptString(cipherText)
```

**Parameters:**
- `cipherText` (str): Encrypted text

**Returns:** Decrypted string

### decryptBytes()
Decrypt to bytes.

```python
decryptBytes(data)
```

**Returns:** Decrypted bytes

### decryptFileToString()
Decrypt file to string.

```python
decryptFileToString(filePath)
```

### decryptFileToBytes()
Decrypt file to bytes.

```python
decryptFileToBytes(filePath)
```

### decryptFile()
Decrypt file to file.

```python
decryptFile(srcPath, destPath)
```

## Usage Example

```python
import androidhelper

droid = androidhelper.Android()

# Encrypt string
encrypted = droid.encryptString("Secret message!").result
print(f"Encrypted: {encrypted}")

# Decrypt string
decrypted = droid.decryptString(encrypted).result
print(f"Decrypted: {decrypted}")

# Encrypt to file
droid.encryptStringToFile("My secret data", "/sdcard/secret.dat")

# Decrypt from file
data = droid.decryptFileToString("/sdcard/secret.dat").result
print(data)
```
