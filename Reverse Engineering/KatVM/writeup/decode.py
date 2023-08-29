import sys


with open(sys.argv[1], "r") as f:
    lines = f.read().splitlines()[9:-3]

final = [""] * 75
order = []
data = []
current_offset = 0
for line in lines:
    cmd, arg = line.split(" ", 1)
    if cmd == "quit":
        continue

    if cmd == "right":
        current_offset += int(arg)
        order.append(current_offset)

    if cmd == "left":
        current_offset -= int(arg)
        order.append(current_offset)

    if cmd == "popeq":
        data.append(arg)


for idx in reversed(order):
    final[idx] = data.pop(0)

print("".join(final))
