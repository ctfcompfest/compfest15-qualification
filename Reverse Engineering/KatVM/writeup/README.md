# Writeup KatVM

Easiest way is to reverse it to source. The VM script is literally its own decompiler, modify it a little bit and you can get the source back.

Change the main script like this, and you get the source!

```python
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
        print(cmd, arg)
```

We can get stuffs back by rebuilding the stack, then reorder the stack according to the offset given by the code. See `decode.py` for solve.
