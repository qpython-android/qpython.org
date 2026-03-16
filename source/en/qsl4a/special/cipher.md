# Cipher API

Encryption and decryption utilities for secure data storage.

## Initialization

### cipherInit()
Initialize the cipher with encryption key and algorithm.

```python
cipherInit(key, algorithm="AES/CBC/PKCS5Padding", encodingFormat="", initialVector="")
```

**Parameters:**
- `key` (str or bytes): Encryption key
- `algorithm` (str): Cipher algorithm (default: "AES/CBC/PKCS5Padding")
- `encodingFormat` (str): Encoding format
- `initialVector` (str or bytes): Initial vector for encryption

**Returns:** Initialization result

**Note:** Must be called before any encrypt/decrypt operations.

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

# Initialize cipher with your encryption key
droid.cipherInit("my_secret_key_1234")

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

# Initialize with custom algorithm and IV
droid.cipherInit(
    key="my_key",
    algorithm="AES/CBC/PKCS5Padding",
    initialVector="0123456789abcdef"
)
```
