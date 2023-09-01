from sage.all import *
from math import log2

def to_bits(m):
    _bin = lambda b: [1 if b & (1 << n) else 0 for n in range(7)]
    return sum([_bin(b) for b in m], [])


def to_bytes(bits):
    _byte = lambda b: sum([b[i] << i for i in range(7)])
    return bytes([_byte(bits[i : i + 7]) for i in range(0, len(bits), 7)])

def attack(a, s):
    """
    Tries to find e_i values such that sum(e_i * a_i) = s.
    This attack only works if the density of the a_i values is < 0.9048.
    More information: Coster M. J. et al., "Improved low-density subset sum algorithms"
    :param a: the a_i values
    :param s: the s value
    :return: the e_i values, or None if the e_i values were not found
    """
    n = len(a)
    d = n / log2(max(a))
    N = ceil(1 / 2 * sqrt(n))
    assert d < 0.9408, f"Density should be less than 0.9408 but was {d}."

    L = matrix(QQ, n + 1, n + 1)
    for i in range(n):
        L[i, i] = 1
        L[i, n] = N * a[i]

    L[n] = [1 / 2] * n + [N * s]

    for v in L.LLL():
        s_ = 0
        e = []
        for i in range(n):
            ei = 1 - (v[i] + 1 / 2)
            if ei != 0 and ei != 1:
                break

            ei = int(ei)
            s_ += ei * a[i]
            e.append(ei)

        if s_ == s:
            return e

with open("output.txt", "r") as f:
    enc = [int(_) for _ in f.readline().split(" = ")[1][1:-2].split(", ")]
    message = b""
    for sentence in f.readlines():
        message += sentence.encode()

# recover public key
msg_bit = to_bits(message)[: (len(message) // 10) * 70]

A = matrix(ZZ, [msg_bit[i : i + 70] for i in range(0, len(msg_bit), 70)])
Y = vector(ZZ, enc[:119])

public_key = list(A.solve_right(Y))
dec = []
for c in enc[119:]:
    try:
        dec += attack(public_key, c)
    except:
        pass

print(to_bytes(dec))