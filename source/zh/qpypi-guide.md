# QPYPI

您可以通过安装包来扩展 QPython 的功能。

## 包安装支持

### 纯 Python 包

QPython 支持使用纯 Python 开发的 Python 包。您可以直接通过 QPython 的 PIP 客户端或仪表盘上的 QPYPI 使用 `pip install` 安装这些包。

### 预编译包

如果某些包（或它们的依赖）是用 Rust/C/C++ 开发的，QPython 无法直接支持它们，因为 QPython 上没有编译器工具链支持。但是，QPython 团队已经预编译了一些常用包，并在 QPython 的 QPYPI/Extensions 中发布，供用户轻松安装。

### 安装预编译包

您可以通过以下方式安装预编译包：

1. **通过 QPython 应用**：直接从 QPython 应用内的 QPYPI 或 Extensions 安装
2. **通过 PyPI**：访问 [https://pypi.org/user/qpythonx/](https://pypi.org/user/qpythonx/) 查看可用的包
3. **通过 pip 命令**：
   - `pip install xxx-qpython` - 带 `-qpython` 后缀的包
   - `pip install xxx-aipy` - 带 `-aipy` 后缀的包（通常是 AI/ML 相关的包）

> **注意**：我们通常根据包的预期用途添加这些后缀之一。

### 请求新包

如果您需要当前不支持的包：

- **在 [qpython.org 项目](https://github.com/qpython-android/qpython.org/issues) 中提出问题**
- QPython 团队将考虑预编译并将其添加到仓库中

获取更多帮助和参与社区的方式，请参阅 [社区与反馈](index.md#社区与反馈) 部分。

> **注意**：由于不同的计算机架构，我们无法保证 QPYPI 包含 PyPI 上的所有包。
