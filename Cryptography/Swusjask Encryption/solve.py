from sage.all import *
from Crypto.Util.number import long_to_bytes, bytes_to_long
from chall import *

F = GF(p)
R = PolynomialRing(F, "w")
w = R.gen()
K = F.extension(w**2 + 69 * w + 6969, "w")
w = K.gen()

FLAG_ENC = open("flag.enc", "rb").read()
blocks = bytes_to_block(FLAG_ENC)
dec = []
for block in blocks:
    a = block % p
    b = block // p
    c_K = a + b * w
    ord = p * p - 1
    d = pow(e, -1, ord)
    m_K = c_K ** d
    coeff = m_K.polynomial().coefficients()
    res = 0
    for i in range(len(coeff) - 1, -1, -1):
        res *= int(p)
        res += int(coeff[i])
    dec.append(int(res))

open("flag_dec.png", "wb").write(block_to_bytes(dec))

