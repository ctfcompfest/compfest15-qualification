import sys


def help_exit():
    print(f"Usage: {sys.argv[0]} <script> <output>")
    exit(1)


def main(source: str, output: str):
    with open(source, "r") as f:
        script = f.read().splitlines()

    fexec = open(output, "wb")
    cmds: dict[str, tuple[int, int]] = {
        "left": (0, 1),
        "right": (1, 1),
        "store": (2, 1),
        "print": (3, 0),
        "input": (4, 0),
        "push": (5, 0),
        "popeq": (6, 1),
        "quit": (7, 0),
    }
    for line in script:
        if not line.strip() or line.startswith("#"):
            continue
        cmd, *arg = line.strip().split(" ", 1)

        cleaned_args: list[str] = []
        for token in arg:
            if token == "#":
                break
            cleaned_args.append(token)

        arg = cleaned_args
        if cmd not in cmds:
            print(f"[ERR] Cannot compile, cannot find command {cmd}.")
            exit(1)

        bytecode, argcount = cmds[cmd]
        if len(arg) != argcount:
            print(
                f"[ERR] Cannot compile, argcount for '{line}'",
                f"does not match expected size {argcount}.",
            )
            exit(1)

        fexec.write(bytecode.to_bytes(1, "little"))
        if len(arg) == 0:
            continue

        if cmd == "store":
            fexec.write(len(arg[0]).to_bytes(8, "little"))
            fexec.write(arg[0].encode())
            continue

        if len(arg) != 0:
            fexec.write(arg[0].encode().ljust(8, b"\0"))

    fexec.close()
    print("Compiled successfully.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        help_exit()

    main(sys.argv[1], sys.argv[2])
