from libnum import s2b
from random import choices
import string

charset = string.ascii_letters
flag = 'sup3r_l0ng_fL46_5o_7hAT_YOu_w0nT_Be_a3le_t0_s0LvE_1t_m4nuALLy_w3ll_tecHnicaLly_u_c4n_bU7_s1mpL3_gdb_scRipt1n9_1s_aLL_You_n33D_a95dff5469'
pairs = [flag[i:i+2][::-1] for i in range(0, len(flag), 2)]
pairs_bin = list(map(s2b, pairs))

lzcnt = lambda s: len(s) - len(s.lstrip('0'))
tzcnt = lambda s: len(s) - len(s.rstrip('0'))

code = "#include <stdio.h>\n"
code += "char input[256];\n"

#################################################
# l = [0, 6, 8, 12, 18, 22, 23, 24, 36, 40, 41, 45, 49, 55, 56, 59, 62]
l = list(range(68))
for i in l:
    code += f"""
int n{i}() {{
    __asm__(
        "xor r10, r10       \\n"
        "tzcnt r10w, r12w   \\n"
        "mov r15, r10       \\n"
    );
}}
"""

for i in l:
    code += f"""
int m{i}() {{
    __asm__(
        "call n{i}          \\n"
        "xor r10, r10       \\n"
        "lzcnt r10w, r12w   \\n"
        "mov r14, r10       \\n"
    );
}}
"""

for i in l:
    code += f"""
int l{i}() {{
    __asm__(
        "push r12   \\n"
        "xor r10, r10           \\n"
        "xor r12, r12           \\n" """
    for j in range(16):
        code += f"""
        "mov r10, 0x10{hex(j)[2:]}         \\n"
        "bextr r12d, r9d, r10d  \\n"
        "call m{i}              \\n" """
        ld_zs = lzcnt(pairs_bin[i][15-j].zfill(16))
        for k in range(17):
            label = ''.join(choices(charset, k=10))
            code += f"""
        "cmp r14, {k}       \\n"
        "jne {label}\\n" """
            if k == ld_zs:
                code += f"""
        "or r11, 0   \\n" """
            else:
                code += f"""
        "or r11, 1  \\n" """
            code += f"""
        "{label}:  \\n" """
        code += """
        "nop\\n" """
        tr_zs = tzcnt(pairs_bin[i][15-j].zfill(16))
        for k in range(17):
            label = ''.join(choices(charset, k=10))
            code += f"""
        "cmp r15, {k}       \\n"
        "jne {label}\\n" """
            if k == tr_zs:
                code += f"""
        "or r11, 0   \\n" """
            else:
                code += f"""
        "or r11, 1  \\n" """
            code += f"""
        "{label}:  \\n" """
        code += """
        "nop\\n" """
    code +="""
        "pop r12\\n"
    );
}
"""

for i in l:
    code += f"""
int kk{i}() {{
    __asm__(
        "call l{i}          \\n"
        "xor r10, r10       \\n"
        "tzcnt r10w, r12w   \\n"
        "mov r15, r10       \\n"
    );
}}
"""

for i in l:
    code += f"""
int jj{i}() {{
    __asm__(
        "call kk{i}          \\n"
        "xor r10, r10       \\n"
        "lzcnt r10w, r12w   \\n"
        "mov r14, r10       \\n"
    );
}}
"""

for i in l:
    code += f"""
int i{i}() {{
    __asm__(
        "push r12   \\n"
        "xor r10, r10           \\n"
        "xor r12, r12           \\n" """
    for j in range(8):
        code += f"""
        "mov r10, 0x20{hex(j*2)[2:]}         \\n"
        "bextr r12d, r9d, r10d  \\n"
        "call jj{i}              \\n" """
        ld_zs = lzcnt(pairs_bin[i][16-j*2-2:16-j*2].zfill(16))
        for k in range(17):
            label = ''.join(choices(charset, k=10))
            code += f"""
        "cmp r14, {k}       \\n"
        "jne {label}\\n" """
            if k == ld_zs:
                code += f"""
        "or r11, 0   \\n" """
            else:
                code += f"""
        "or r11, 1  \\n" """
            code += f"""
        "{label}:  \\n" """
        code += """
        "nop\\n" """
        tr_zs = tzcnt(pairs_bin[i][16-j*2-2:16-j*2].zfill(16))
        for k in range(17):
            label = ''.join(choices(charset, k=10))
            code += f"""
        "cmp r15, {k}       \\n"
        "jne {label}\\n" """
            if k == tr_zs:
                code += f"""
        "or r11, 0   \\n" """
            else:
                code += f"""
        "or r11, 1  \\n" """
            code += f"""
        "{label}:  \\n" """
        code += """
        "nop\\n" """
    code +="""
        "pop r12\\n"
    );
}
"""

for i in l:
    code += f"""
int h{i}() {{
    __asm__(
        "call i{i}          \\n"
        "xor r10, r10       \\n"
        "tzcnt r10w, r12w   \\n"
        "mov r15, r10       \\n"
    );
}}
"""

for i in l:
    code += f"""
int g{i}() {{
    __asm__(
        "call h{i}          \\n"
        "xor r10, r10       \\n"
        "lzcnt r10w, r12w   \\n"
        "mov r14, r10       \\n"
    );
}}
"""

for i in l:
    code += f"""
int f{i}() {{
    __asm__(
        "push r12\\n"
        "xor r10, r10           \\n"
        "xor r12, r12           \\n" """
    for j in range(4):
        code += f"""
        "mov r10, 0x40{hex(j*4)[2:]}         \\n"
        "bextr r12d, r9d, r10d  \\n"
        "call g{i}              \\n" """
        ld_zs = lzcnt(pairs_bin[i][16-j*4-4:16-j*4].zfill(16))
        for k in range(17):
            label = ''.join(choices(charset, k=10))
            code += f"""
        "cmp r14, {k}       \\n"
        "jne {label}\\n" """
            if k == ld_zs:
                code += f"""
        "or r11, 0   \\n" """
            else:
                code += f"""
        "or r11, 1  \\n" """
            code += f"""
        "{label}:  \\n" """
        code += """
        "nop\\n" """
        tr_zs = tzcnt(pairs_bin[i][16-j*4-4:16-j*4].zfill(16))
        for k in range(17):
            label = ''.join(choices(charset, k=10))
            code += f"""
        "cmp r15, {k}       \\n"
        "jne {label}\\n" """
            if k == tr_zs:
                code += f"""
        "or r11, 0   \\n" """
            else:
                code += f"""
        "or r11, 1  \\n" """
            code += f"""
        "{label}:  \\n" """
        code += """
        "nop\\n" """
    code +="""
        "pop r12\\n"
    );
}
"""

for i in l:
    code += f"""
int e{i}() {{
    __asm__(
        "call f{i}          \\n"
        "xor r10, r10       \\n"
        "tzcnt r10w, r12w   \\n"
        "mov r15, r10       \\n"
    );
}}
"""

for i in l:
    code += f"""
int d{i}() {{
    __asm__(
        "call e{i}          \\n"
        "xor r10, r10       \\n"
        "lzcnt r10w, r12w   \\n"
        "mov r14, r10       \\n"
    );
}}
"""


for i in l:
    code += f"""
int c{i}() {{
    __asm__(
        "xor r10, r10           \\n"
        "xor r12, r12           \\n" """
    for j in range(2):
        code += f"""
        "mov r10, 0x80{hex(j*8)[2:]}         \\n"
        "bextr r12d, r9d, r10d  \\n"
        "call d{i}              \\n" """
        ld_zs = lzcnt(pairs_bin[i][16-j*8-8:16-j*8].zfill(16))
        for k in range(17):
            label = ''.join(choices(charset, k=10))
            code += f"""
        "cmp r14, {k}       \\n"
        "jne {label}\\n" """
            if k == ld_zs:
                code += f"""
        "or r11, 0   \\n" """
            else:
                code += f"""
        "or r11, 1  \\n" """
            code += f"""
        "{label}:  \\n" """
        code += """
        "nop\\n" """
        tr_zs = tzcnt(pairs_bin[i][16-j*8-8:16-j*8].zfill(16))
        for k in range(17):
            label = ''.join(choices(charset, k=10))
            code += f"""
        "cmp r15, {k}       \\n"
        "jne {label}\\n" """
            if k == tr_zs:
                code += f"""
        "or r11, 0   \\n" """
            else:
                code += f"""
        "or r11, 1  \\n" """
            code += f"""
        "{label}:  \\n" """
        code += """
        "nop\\n" """
    code +="""
    );
}
"""

for i in l:
    code += f"""
int b{i}() {{
    __asm__(
        "call c{i}          \\n"
        "xor r10, r10       \\n"
        "tzcnt r10w, r9w   \\n"
        "mov r15, r10       \\n"
    );
}}
"""

for i in l:
    code += f"""
int a{i}() {{
    __asm__(
        "call b{i}          \\n"
        "xor r10, r10       \\n"
        "lzcnt r10w, r9w    \\n"
        "mov r14, r10       \\n" """
    ld_zs = lzcnt(pairs_bin[i])
    for k in range(17):
        label = ''.join(choices(charset, k=10))
        code += f"""
        "cmp r14, {k}       \\n"
        "jne {label}\\n" """
        if k == ld_zs:
            code += f"""
        "or r11, 0   \\n" """
        else:
            code += f"""
        "or r11, 1  \\n" """
        code += f"""
        "{label}:  \\n" """
    code += """
        "nop\\n" """
    tr_zs = tzcnt(pairs_bin[i])
    for k in range(17):
        label = ''.join(choices(charset, k=10))
        code += f"""
        "cmp r15, {k}       \\n"
        "jne {label}\\n" """
        if k == tr_zs:
            code += f"""
        "or r11, 0   \\n" """
        else:
            code += f"""
        "or r11, 1  \\n" """
        code += f"""
        "{label}:  \\n" """
    code += """
        "nop\\n" 
        "mov r9, r11\\n" """

    code +="""
    );
}
"""


#################################################

code +=f"""
int func(char* string) {{
    __asm__(
        "xor r8, r8             \\n"
        "xor r9, r9             \\n"
        "mov r9w, word ptr[rdi] \\n"
        "call a0                \\n"
        "or r8, r9              \\n" """
for i in l[1:]:
    code += f"""
        "add rdi, 2             \\n"
        "mov r9w, word ptr[rdi] \\n"
        "call a{i}               \\n"
        "or r8, r9              \\n" """
code += """
    );
}
"""

code += """
void main() {
   asm("push [rbp+8]");
   asm("ret"); 

   printf("Enter the flag: ");
   scanf("%s", input);

   func(input);
   __asm__(
    "test r8, r8\\n"
    "jne else\\n"
   );
   puts("Correct.");
   asm("jmp end");
   asm("else:");
   puts("Incorrect.");
   asm("end:");
}"""

with open('chall.c', 'w') as f:
    f.write(code)