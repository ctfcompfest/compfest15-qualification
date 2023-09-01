from io import BufferedReader
import os
import sys
from typing import Callable


# "command_name": (command_function, required_argcount)
cmd_map: dict[str, tuple[Callable, int]] = {
    "left": (lambda vm: vm.left, 1),
    "right": (lambda vm: vm.right, 1),
    "store": (lambda vm: vm.store, 1),
    "print": (lambda vm: vm.print, 0),
    "input": (lambda vm: vm.input, 0),
    "push": (lambda vm: vm.push, 0),
    "popeq": (lambda vm: vm.popeq, 1),
    "quit": (lambda vm: exit, 0),
}
# Just the list above, for easier bytecode translation
cmds = ["left", "right", "store", "print", "input", "push", "popeq", "quit"]


def is_eof(f: BufferedReader):
    cur = f.tell()
    f.seek(0, os.SEEK_END)
    end = f.tell()
    f.seek(cur, os.SEEK_SET)
    return cur == end


def help_exit():
    print(f"Usage: {sys.argv[0]} <kbfile> <katfile>")
    exit(1)


def read_instruction(f: BufferedReader) -> tuple[str, str] | str:
    bytecode = f.read(1)
    cmd = cmds[int.from_bytes(bytecode, "little")]
    if cmd == "store":
        str_len = int.from_bytes(f.read(8), "little")
        return cmd, f.read(str_len).decode()

    if cmd_map[cmd][1] == 0:
        return cmd, ""

    return cmd, f.read(8).decode().strip("\x00")


def main(execfile: str, katfile: str):
    fw = open(katfile, "w")
    f = open(execfile, "rb")
    while not is_eof(f):
        try:
            cmd, arg = read_instruction(f)
        except:
            print("[ERR] Invalid bytecode")
            break
        print(cmd, arg, file=fw)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        help_exit()
    main(sys.argv[1], sys.argv[2])
