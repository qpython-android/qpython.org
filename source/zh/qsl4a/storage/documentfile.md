# DocumentFile API

使用 SAF（存储访问框架）进行文件操作，支持 Android 4.4+。

## 目录操作

### documentFileMkdir()
创建目录。

```python
documentFileMkdir(Dir)
```

**参数：**
- `Dir` (str): 目录路径

**返回：** 如果成功则为 True

### documentFileListFiles()
列出目录中的文件。

```python
documentFileListFiles(Folder)
```

**返回：** 文件列表

## 文件操作

### documentFileExists()
检查文件或目录是否存在。

```python
documentFileExists(path)
```

**参数：**
- `path` (str): 文件或目录路径

**返回：** 如果存在则为 True，否则为 False

### documentFileIsFile()
检查路径是否是文件。

```python
documentFileIsFile(path)
```

**参数：**
- `path` (str): 要检查的路径

**返回：** 如果是文件则为 True，如果不是文件则为 False，如果不存在则为 None

### documentFileIsDirectory()
检查路径是否是目录。

```python
documentFileIsDirectory(path)
```

**参数：**
- `path` (str): 要检查的路径

**返回：** 如果是目录则为 True，如果不是目录则为 False，如果不存在则为 None

### documentFileDelete()
删除文件或目录。

```python
documentFileDelete(FileOrTree)
```

**返回：** 如果成功则为 True

### documentFileRenameTo()
重命名或移动文件。

```python
documentFileRenameTo(Src, Dest)
```

**返回：** 如果成功则为 True

### documentFileCopy()
复制文件。

```python
documentFileCopy(SrcFileOrTree, DestFileOrTree)
```

## 流操作

### documentFileInputStream()
读取文件内容。

```python
documentFileInputStream(srcFile, EncodingFormat="", skip=None, length=None)
```

**参数：**
- `srcFile` (str): 源文件
- `EncodingFormat` (str): "UTF-8"、"GBK"、"Base64" 或空字符串表示字节
- `skip` (int): 从开头跳过的字节数
- `length` (int): 读取长度

**返回：** 文件内容

### documentFileOutputStream()
写入文件内容。

```python
documentFileOutputStream(destFile, src, EncodingFormat="", append=None)
```

**参数：**
- `destFile` (str): 目标文件
- `src`: 要写入的数据
- `EncodingFormat` (str): 编码格式
- `append` (bool): 追加模式

## 文件信息

### documentFileLength()
获取文件大小（字节）。

```python
documentFileLength(path)
```

**参数：**
- `path` (str): 文件路径

**返回：** 文件大小（字节）（如果不存在则为 0）

### documentFileLastModified()
获取最后修改时间。

```python
documentFileLastModified(path)
```

**参数：**
- `path` (str): 文件路径

**返回：** 时间戳（如果不存在则为 0）

### documentFileGetStat()
获取全面的文件统计信息。

```python
documentFileGetStat(path)
```

**参数：**
- `path` (str): 文件路径

**返回：** 包含长度、最后修改时间和读/写权限的字典，如果不存在则为 None

## URI 操作

### documentFileGetUri()
从路径获取 URI。

```python
documentFileGetUri(path, isDirectory=None)
```

### documentFileShowOpen()
显示文件选择器。

```python
documentFileShowOpen()
```

**返回：** 选择的文件 URI

## 使用示例

```python
import androidhelper

droid = androidhelper.Android()

# 创建目录
droid.documentFileMkdir("/sdcard/MyFolder")

# 列出文件
files = droid.documentFileListFiles("/sdcard").result
for f in files:
    print(f)

# 读取文件
content = droid.documentFileInputStream(
    "/sdcard/test.txt",
    EncodingFormat="UTF-8"
).result
print(content)

# 写入文件
droid.documentFileOutputStream(
    "/sdcard/output.txt",
    "Hello World",
    EncodingFormat="UTF-8"
)
```
