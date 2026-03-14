# DocumentFile API

File operations with SAF (Storage Access Framework) support for Android 4.4+.

## Directory Operations

### documentFileMkdir()
Create directory.

```python
documentFileMkdir(Dir)
```

**Parameters:**
- `Dir` (str): Directory path

**Returns:** True if success

### documentFileListFiles()
List files in directory.

```python
documentFileListFiles(Folder)
```

**Returns:** List of files

## File Operations

### documentFileDelete()
Delete file or directory.

```python
documentFileDelete(FileOrTree)
```

**Returns:** True if success

### documentFileRenameTo()
Rename or move file.

```python
documentFileRenameTo(Src, Dest)
```

**Returns:** True if success

### documentFileCopy()
Copy file.

```python
documentFileCopy(SrcFileOrTree, DestFileOrTree)
```

## Stream Operations

### documentFileInputStream()
Read file content.

```python
documentFileInputStream(srcFile, EncodingFormat="", skip=None, length=None)
```

**Parameters:**
- `srcFile` (str): Source file
- `EncodingFormat` (str): "UTF-8", "GBK", "Base64", or "" for bytes
- `skip` (int): Skip bytes from start
- `length` (int): Read length

**Returns:** File content

### documentFileOutputStream()
Write file content.

```python
documentFileOutputStream(destFile, src, EncodingFormat="", append=None)
```

**Parameters:**
- `destFile` (str): Destination file
- `src`: Data to write
- `EncodingFormat` (str): Encoding format
- `append` (bool): Append mode

## URI Operations

### documentFileGetUri()
Get URI from path.

```python
documentFileGetUri(path, isDirectory=None)
```

### documentFileShowOpen()
Show file picker.

```python
documentFileShowOpen()
```

**Returns:** Selected file URI

## Usage Example

```python
import androidhelper

droid = androidhelper.Android()

# Create directory
droid.documentFileMkdir("/sdcard/MyFolder")

# List files
files = droid.documentFileListFiles("/sdcard").result
for f in files:
    print(f)

# Read file
content = droid.documentFileInputStream(
    "/sdcard/test.txt",
    EncodingFormat="UTF-8"
).result
print(content)

# Write file
droid.documentFileOutputStream(
    "/sdcard/output.txt",
    "Hello World",
    EncodingFormat="UTF-8"
)
```
