# QPYPI

You can extend your QPython capabilities by installing packages.

## Package Installation Support

### Pure Python Packages

QPython supports Python packages developed with pure Python. You can install these packages directly using `pip install` through QPython's PIP Client or QPYPI on dashboard.

### Pre-compiled Packages

If some packages (or their dependencies) are developed with Rust/C/C++, QPython cannot support them directly because there is no compiler toolchain support on QPython. However, the QPython team has pre-compiled some commonly used packages and published them in QPython's QPYPI/Extensions for users to install easily.

### Installing Pre-compiled Packages

You can install pre-compiled packages in the following ways:

1. **Through QPython App**: Install directly from QPYPI or Extensions within the QPython app
2. **Through PyPI**: Visit [https://pypi.org/user/qpythonx/](https://pypi.org/user/qpythonx/) to view available packages
3. **Via pip command**:
   - `pip install xxx-qpython` - Packages with the `-qpython` suffix
   - `pip install xxx-aipy` - Packages with the `-aipy` suffix (typically AI/ML related packages)

> **Note**: We usually add one of these suffixes based on the package's intended use case.

### Requesting New Packages

If you need a package that is not currently supported:

- **Raise an issue** in the QPYPI project
- The QPython team will consider pre-compiling and adding it to the repository

Because of different computer architectures, we cannot guarantee that QPYPI includes all packages from PyPI.