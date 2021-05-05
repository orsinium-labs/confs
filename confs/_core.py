import typing
from configparser import ConfigParser
from pathlib import Path
import toml


FILES = {
    '.flake8': 'flake8',
    '.yamllint': 'yamllint',
    '.yamllint.yaml': 'yamllint',
    '.yamllint.yml': 'yamllint',
    '.markdownlint.jsonc': 'markdownlint',
    '.markdownlint.yaml': 'markdownlint',
    '.shellcheckrc': 'shellcheck',
}


def _from_ini(path: Path) -> typing.Iterator[str]:
    if not path.exists():
        return
    config = ConfigParser()
    config.read(str(path))
    for section in config.sections():
        section = section.split('.')[0]
        section = section.split(':')[0]
        yield section


def _from_toml(path: Path) -> typing.Iterator[str]:
    if not path.exists():
        return
    with path.open('r', encoding='utf8') as stream:
        data = toml.load(stream)
    data = data.get('tool', {})
    yield from data


def _from_filenames(path: Path) -> typing.Iterator[str]:
    for file_name, tool_name in FILES.items():
        if (path / file_name).exists():
            yield tool_name


def get_tools(path: Path) -> typing.Iterator[str]:
    if not path.is_dir():
        return
    yield from _from_ini(path / 'setup.cfg')
    yield from _from_ini(path / 'tox.ini')
    yield from _from_toml(path / 'pyproject.toml')
    yield from _from_filenames(path)
