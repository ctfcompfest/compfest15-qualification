from io import BufferedReader
import os
import sys
from typing import Callable


class KatVM:
    tape: list[str] = [""]
    memory: list[str] = []
    pointer: int = 0

    def left(self, value: str | int):
        val = int(value)
        for _ in range(val):
            if self.pointer == 0:
                self.tape.insert(0, "")
            else:
                self.pointer -= 1

    def right(self, value: str | int):
        val = int(value)
        for _ in range(val):
            if self.pointer == len(self.tape) - 1:
                self.tape.append("")
            self.pointer += 1

    def store(self, string: str):
        for i in range(len(string)):
            self.tape[self.pointer] = string[i]
            self.right(1)
        self.tape[self.pointer] = ""

    def print(self):
        while c := self.tape[self.pointer]:
            print(c, end="", flush=True)
            self.right(1)
        print(flush=True)

    def input(self):
        self.store(input())

    def push(self):
        self.memory.append(self.tape[self.pointer])

    def popeq(self, value: str):
        return self.memory.pop() == value


# "command_name": (command_function, required_argcount)
cmd_map: dict[str, tuple[Callable[[KatVM], Callable], int]] = {
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
    print(f"Usage: {sys.argv[0]} <katfile>")
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


def main(execfile: str):
    vm = KatVM()
    f = open(execfile, "rb")
    skip_next = False
    while not is_eof(f):
        try:
            cmd, arg = read_instruction(f)
        except:
            print("[ERR] Invalid bytecode")
            break

        if skip_next:
            skip_next = False
            continue

        func = cmd_map[cmd][0]
        if arg:
            res = func(vm)(arg)
            if res == True:
                skip_next = True
        else:
            func(vm)()
    f.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        help_exit()
    main(sys.argv[1])
