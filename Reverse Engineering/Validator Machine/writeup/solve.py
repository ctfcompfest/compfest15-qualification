from libnum import b2s

class GdbScript(gdb.Command):
    def __init__ (self):
        super (GdbScript, self).__init__ ("solve", gdb.COMMAND_OBSCURE)
   
    def invoke (self):
        gdb.execute('set disassembly-flavor intel')
        bp = 0x555555790896
        for _ in range(68):
            gdb.execute(f'b *{bp}')
            bp += 0x10

        flag = ''

        gdb.execute(f'r < <(echo "")')
        for _ in range(68):
            count = 0
            while count != 9:
                gdb.execute('si')
                if 'call' in gdb.execute('x/i $rip', to_string=True):
                    count += 1
            gdb.execute('si')
            for _ in range(6): gdb.execute('ni')
            bits = [0 for _ in range(16)]
            temp = []
            i = 14
            while not all(bits):
                gdb.execute('ni')
                for _ in range(17):
                    gdb.execute('ni')
                    gdb.execute('ni')
                    insts = gdb.execute('x/3i $rip', to_string=True)
                    if 'r11,0x0' in insts:
                        ld_zs = int(insts.split('\n')[0].split(',')[1], 16)

                gdb.execute('ni')
                gdb.execute('ni')

                if ld_zs == 14:
                    bits[i] = '1'
                else:
                    bits[i] = '0'

                for _ in range(17):
                    gdb.execute('ni')
                    gdb.execute('ni')
                    insts = gdb.execute('x/3i $rip', to_string=True)
                    if 'r11,0x0' in insts:
                        tr_zs = int(insts.split('\n')[0].split(',')[1], 16)
                for _ in range(4):gdb.execute('ni')
                if tr_zs == 0:
                    bits[i+1] = '1'
                else:
                    bits[i+1] = '0'

                i -= 2

            f = open('flag.txt', 'w')
            flag += b2s(''.join(bits))[::-1].decode()
            f.write(flag)
            f.close()
            gdb.execute('c')
            

GdbScript()