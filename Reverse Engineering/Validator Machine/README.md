# Validator Machine

by ivanox

---

## Flag

```
COMPFEST15{sup3r_l0ng_fL46_5o_7hAT_YOu_w0nT_Be_a3le_t0_s0LvE_1t_m4nuALLy_w3ll_tecHnicaLly_u_c4n_bU7_s1mpL3_gdb_scRipt1n9_1s_aLL_You_n33D_a95dff5469}
```

## Flag (mirror)

```
COMPFEST15{d68be8c4f7a07c86b9911ed0c48524a5326de82d2db28612aae7245227a7a4fba3819df16351e232c27790ec6d24133ecfc559d5a6361db222b9e8612ce6ef3a25914dfe}
```

## Description
Just a simple flag validator machine.

> Note: Wrap the flag with COMPFEST15{}

## Difficulty
Tingkat kesulitan soal: medium-hard

## Hints
> Intentionally left empty

## Tags
vm, gdb scripting, anti-analysis

## Deployment
```text
python3 gen_chall.py && \
gcc -masm=intel chall.c -o chall -z execstack -s && \
objcopy --writable-text --set-section-flags .text=CONTENTS,ALLOC,LOAD,CODE chall && \
./writable chall
```

## Notes
> Intentionally left empty
