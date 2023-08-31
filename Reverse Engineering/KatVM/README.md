# KatVM

by rorre

---

## Flag

```
COMPFEST15{r3Ad1ng_byt3C0de_c4n_b3_r3ally_H4rd_y0u_kNow}
```

## Description

I made my own language! It's very simple, yet effective in comparing things. It has turing machine like properties as well.

Here are the instructions available, write in just like how you write assembly or script, its top to down:

- `left <N>`, `right <N>`: Move the tape head to left or right by N
- `store <STRING>`: Store string to from current head, the head will move right after the string
- `print`: Print from head to next empty
- `input`: Input from stdin and store it in current head, the head will move right after the string
- `push`: Push current head to stack
- `popeq <CHAR>`: Pop current stack, and compare the character with given char. If true, it will skip next instruction
- `quit`: Exit

You may write it the code in a `.kat` file, and you can compile it with `python build.py yourfile.kat output.kb`. Then execute it
with `python katvm.py output.kb`.

## Difficulty

Tingkat kesulitan soal: medium-hard

## Hints

- Maybe the vm runner script could help in parsing

## Tags

assembly, compiler
