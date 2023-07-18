from sage.all import *
from Crypto.Util.number import long_to_bytes, bytes_to_long

def bytes_to_block(msg: bytes):
    res = []
    msg_int = bytes_to_long(msg)
    while msg_int:
        res.append(msg_int % (p**2))
        msg_int //= p**2
    return res


def block_to_bytes(blocks: list[int]):
    res = 0
    for i in range(len(blocks) - 1, -1, -1):
        res *= p**2
        res += blocks[i]
    return long_to_bytes(res)

p = 1179478847235411356076287763101027881
e = 0x10001
F = GF(p)
R = PolynomialRing(F, "w")
w = R.gen()
K = F.extension(w**2 + 69 * w + 6969, "w")
w = K.gen()
ord = p * p - 1
d = pow(e, -1, ord)

FLAG_ENC = open("flag.enc", "rb").read()
blocks = bytes_to_block(FLAG_ENC)
dec = []
for block in blocks:
    a = block % p
    b = block // p
    c_K = a + b * w
    m_K = c_K ** d
    coeff = m_K.polynomial().coefficients()
    res = 0
    for i in range(len(coeff) - 1, -1, -1):
        res *= int(p)
        res += int(coeff[i])
    dec.append(int(res))

open("flag_dec.png", "wb").write(block_to_bytes(dec))

