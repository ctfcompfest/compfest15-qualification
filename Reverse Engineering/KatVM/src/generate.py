import random

f = open("check.kat", "w")

flag = "meowmeow~COMPFEST15{r3Ad1ng_byt3C0de_c4n_b3_r3ally_H4rd_y0u_kNow}"
idxs = [i for i in range(len(flag))]
random.shuffle(idxs)

print(
    f"""store Hello!
left 6
print
store Give me your secret!
left 20
print
right 1
input
left {len(flag)}""",
    file=f,
)

current_offset = 0
for idx in idxs:
    if current_offset > idx:
        print(f"left {current_offset - idx}", file=f)
        current_offset = idx
    elif current_offset < idx:
        print(f"right {idx - current_offset}", file=f)
        current_offset = idx

    print("push", file=f)

for idx in reversed(idxs):
    print(f"popeq {flag[idx]}", file=f)
    print("quit", file=f)

print(
    """store Thanks!
left 7
print""",
    file=f,
)

f.close()
