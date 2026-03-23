# Terminal - Python Command Line Tools

Terminal is one of the most frequently used features in QPython. It's a powerful tool for exploring Python features and libraries, experimenting with new syntax, and managing packages.

![Terminal](static/terminal_demo.jpg)

## Overview

QPython provides multiple terminal options to suit different needs:

- **QPython Shell Terminal** – The standard Python shell for quick exploration
- **IPython Interactive Interpreter** – A more powerful and feature-rich interactive interpreter
- **PIP Client** – Command-line tool for managing Python packages

## Accessing Terminal

### Quick Access

1. Open QPython and go to the **Dashboard**
2. **Click** the Terminal icon to enter the default QPython Shell Terminal

### Advanced Options (Long Press)

On the Dashboard, **long press** the Terminal icon to access additional options:

- **QPython Shell Terminal** – Launch the standard Python shell
- **IPython Interactive Interpreter** – Launch IPython with advanced features like tab completion, syntax highlighting, and command history
- **PIP Client** – Launch the package management interface

## QPython Shell Terminal

The QPython Shell Terminal provides a quick way to execute Python commands and explore Python features.

### Features

- Immediate command execution
- Basic Python interpreter functionality
- Access to Python built-in functions and standard library
- Perfect for quick tests and experiments

### Example Usage

```python
>>> print("Hello from QPython!")
Hello from QPython!
>>> import math
>>> math.sqrt(16)
4.0
>>> [x**2 for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

## IPython Interactive Interpreter

IPython offers a much more powerful interactive Python experience with enhanced features.

### Features

- **Tab Completion** – Automatically complete variable names, module attributes, and file paths
- **Command History** – Navigate through previous commands with up/down arrows
- **Syntax Highlighting** – Color-coded output for better readability
- **Magic Commands** – Special commands prefixed with `%` for common tasks
- **Object Introspection** – Easily explore objects and their attributes

### Example Usage

```python
In [1]: import numpy as np

In [2]: arr = np.array([1, 2, 3, 4, 5])

In [3]: arr?
Type:            ndarray
String form:     [1 2 3 4 5]
Length:          5
...

In [4]: %timeit arr ** 2
The slowest run took 12.34 microseconds...
```

## PIP Client

The PIP Client provides command-line access to Python package management.

### Features

- Install packages from PyPI
- View installed packages
- Upgrade packages
- Uninstall packages
- Search for packages

### Common Commands

```bash
# Install a package
pip install requests

# List installed packages
pip list

# Upgrade a package
pip install --upgrade requests

# Uninstall a package
pip uninstall requests

# Search for packages
pip search json
```

### Usage Tips

- Long press to access PIP Client from the Dashboard
- Use `pip help` to see all available commands
- Some commands may require administrator privileges

## Choosing the Right Tool

| Tool | Best For |
|------|----------|
| Shell Terminal | Quick calculations, simple scripts, testing snippets |
| IPython | Complex exploration, data analysis, interactive debugging |
| PIP Client | Installing/updating packages, checking dependencies |

## Learn More

- [Python Documentation](https://docs.python.org/3.12/) – Official Python language and library reference
- [IPython Documentation](https://ipython.readthedocs.io/) – Advanced interactive Python features
- [PyPI Guide](qpypi-guide.md) – Managing Python packages in QPython
