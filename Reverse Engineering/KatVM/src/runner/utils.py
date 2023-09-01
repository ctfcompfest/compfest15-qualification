from io import BufferedReader
import os
import sys

from typing import Callable


cmds: list[tuple[Callable, int]] = [
    (lambda vm: vm.left, 1),
    (lambda vm: vm.right, 1),
    (lambda vm: vm.store, 1),
    (lambda vm: vm.print, 0),
    (lambda vm: vm.input, 0),
    (lambda vm: vm.push, 0),
    (lambda vm: vm.popeq, 1),
    (lambda vm: exit, 0),
]


def is_eof(f: BufferedReader):
    cur = f.tell()
    f.seek(0, os.SEEK_END)
    end = f.tell()
    f.seek(cur, os.SEEK_SET)
    return cur == end


def help_exit():
    print(f"Usage: {sys.argv[0]} <kbfile>")
    exit(1)


def read_instruction(f: BufferedReader) -> tuple[tuple[Callable, int], str]:
    bytecode = f.read(1)
    num = int.from_bytes(bytecode, "little")
    cmd = cmds[num]
    if num == 2:
        str_len = int.from_bytes(f.read(8), "little")
        return cmd, f.read(str_len).decode()

    if cmd[1] == 0:
        return cmd, ""

    return cmd, f.read(8).decode().strip("\x00")
