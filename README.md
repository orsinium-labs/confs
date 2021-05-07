# confs

CLI tool that lists tools for which the given project has configuration files.

For example, if the project has `.isort.cfg` file or `[tool.isort]` section in `pyproject.toml`, confs will detect that the project uses [isort](https://pycqa.github.io/isort/). A possible use-case is to implement CI jobs for linters that are run only if the corresponding configuration file is represented in the project.

## Installation

```bash
python3 -m pip install --user confs
```

## CLI usage

+ `confs list` - list tools configured in the current directory.
+ `confs list --path=/path/to/project/` - list tools configured in the specified directory.
+ `confs has flake8` - check if the project has `flake8` configured. The exit code is 1 if the tool is not configured.

## API usage

```python
from pathlib import Path
from confs import get_tools

path = Path('.')
print(get_tools(path))
```
