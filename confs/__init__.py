"""
CLI tool that lists tools for which the given project has configuration files.
"""

from ._core import get_tools
from ._cli import entrypoint


__version__ = '1.0.0'
__all__ = ['get_tools', 'entrypoint']
