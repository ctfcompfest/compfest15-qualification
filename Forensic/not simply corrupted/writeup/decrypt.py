from binascii import *
from re import *

masuk = open("../public/cat.png", 'rb')
masuk_hex = []
output = open("chall.png", 'wb')

for i in masuk.read():
    masuk_hex.append(f"{i:02x}")

masuk_hex = [ ''.join(x) for x in zip(masuk_hex[0::4], masuk_hex[1::4], masuk_hex[2::4], masuk_hex[3::4]) ] 
for i in masuk_hex:
    hexx = hex(int(i, 2))
    hexx = hexx[2:]
    if len(hexx) % 2 == 1:
        hexx = '0' + hexx
    output.write(unhexlify(hexx))