from binascii import *
from re import *

masuk = open("chall.png", 'rb')
output = open("cat.png", 'wb')

#To Hex
masuk_hex = str(hexlify(masuk.read()))
masuk_split = findall('..?', masuk_hex)
masuk_split = masuk_split[1:-1]

for i in masuk_split:
    #Hex literal to Binary
    binary = bin(int(i, 16))
    binary = "0"*(8-len(binary[2:])) + binary[2:]
    output.write(unhexlify(binary))