import sys
import traceback

from utils import is_eof, read_instruction, help_exit
from vm import KatVM


def run(execfile: str):
    vm = KatVM()
    f = open(execfile, "rb")
    skip_next = False
    while not is_eof(f):
        cmd, arg = read_instruction(f)
        if skip_next:
            skip_next = False
            continue

        func = cmd[0]
        if arg:
            res = func(vm)(arg)
            if res == True:
                skip_next = True
        else:
            func(vm)()
    f.close()


def main():
    if len(sys.argv) != 2:
        help_exit()
    try:
        run(sys.argv[1])
    except:
        print("Segmentation fault")
