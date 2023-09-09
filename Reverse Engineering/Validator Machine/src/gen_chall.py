from libnum import s2b
from random import choices
import string

charset = string.ascii_letters
flag = 'd68be8c4f7a07c86b9911ed0c48524a5326de82d2db28612aae7245227a7a4fba3819df16351e232c27790ec6d24133ecfc559d5a6361db222b9e8612ce6ef3a25914dfe'
fake_flag1 = '94211497f535b3ac1b9af8d350b8f3cb23f95b166a0e12971ed143e8d3c5d9ee228c2aa89d755cd857e0edde08b5dadd661fe02f6a3b524da92b1a090e16ad2e330c4933'
fake_flag2 = 'ab5ce72a3a67aa732a6e883ec07a5db0706f4d785481538537e2e137b52bf34ff2c3f9e21785340bb426c8c295119eda88e42748b3e5a40d2e0820d1f67d1057938ae52e'
flag += fake_flag1 + fake_flag2
pairs = [flag[i:i+2][::-1] for i in range(0, len(flag), 2)]
pairs_bin = list(map(s2b, pairs))

lzcnt = lambda s: len(s) - len(s.lstrip('0'))
tzcnt = lambda s: len(s) - len(s.rstrip('0'))

code = """
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char input[256];

void detect_debugger() __attribute__((constructor));

void gadget() {
"""

for i in range(68):
    code += f'\tasm("call a{i}");\n'

for i in range(68*2, 68*3):
    code += f'\tasm("call a{i}");\n'

code += "}\n"
#################################################
l = list(range(68*3))
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
}"""

#################################################

code +=f"""
int func(char* string) {{
    __asm__(
        "xor r8, r8             \\n"
        "xor r9, r9             \\n"
        "mov r9w, word ptr[rdi] \\n"
        "call a68                \\n"
        "or r8, r9              \\n" """
for i in l[68+1:2*len(l)//3]:
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
void detect_debugger(){
    int offsets[68*3];
    """

x = 17
for i in range(68):
    code += f'\toffsets[{i}] = (int)(&a{i} - (&func + {x}+ 10));\n'
    x += 16

x = 17
for i in range(68*2, 68*3):
    code += f'\toffsets[{i}] = (int)(&a{i} - (&func + {x}+10));\n'
    x += 16

    
code += """
    const unsigned char sc[] = {72, 49, 192, 72, 137, 194, 72, 137, 198, 72, 137, 199, 4, 101, 15, 5, 195};
    int (*zzzz)() = (int(*)()) sc;
    int i = zzzz();
    if (i < 0) {
    """
x = 23
for i in range(68*2, 68*3):
    code += f'\t\tmemcpy(*func+{x}, offsets+{i}, 4);\n'
    x += 16

code += "\t} else {\n"

x = 23
for i in range(68):
    code += f'\t\tmemcpy(*func+{x}, offsets+{i}, 4);\n'
    x += 16

code += "\t}\n}\n"

code += """
void main() {
   printf("Enter the flag: ");
   scanf("%255s", input);

   func(input);
   __asm__(
    "test r8, r8\\n"
    "jne else\\n"
   );
   puts("Correct.");
   asm("jmp end2");
   asm("else:");
   puts("Incorrect.");
   asm("end2:");
}"""


with open('chall.c', 'w') as f:
    f.write(code)