import sys
import typing
from argparse import ArgumentParser
from pathlib import Path
from ._core import get_tools


def cmd_list(path: Path) -> int:
    for tool in sorted(set(get_tools(path))):
        print(tool)
    return 0


def cmd_has(path: Path, name: str) -> int:
    if name in set(get_tools(path)):
        print('yes')
        return 0
    print('no')
    return 1


def main(argv: typing.List[str]) -> int:
    parser = ArgumentParser()
    parser.add_argument('cmd', choices=['list', 'has'])
    parser.add_argument('--path', type=Path, default=Path())
    args, _ = parser.parse_known_args(argv)
    if args.cmd == 'list':
        args = parser.parse_args(argv)
        return cmd_list(path=args.path)
    if args.cmd == 'has':
        parser.add_argument('name')
        args = parser.parse_args(argv)
        return cmd_has(path=args.path, name=args.name)
    raise RuntimeError('unreachable')


def entrypoint() -> typing.NoReturn:
    sys.exit(main(sys.argv[1:]))
