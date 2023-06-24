from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime, GCD
from sage.all import *

FLAG = b"COMPFEST15{REDACTED}".ljust(256, b"\x00")

test = 0
while True:
    # all parameter not publicly known
    p = getPrime(1024)
    q = getPrime(1024)
    n = p * q
    phi = (p - 1) * (q - 1)

    # user can input max 3 public exponent
    e2 = 5
    e3 = 7
    e4 = 11
    e1 = e2 * e3 * e4
    if GCD(e1, phi) == 1:
        print(test)
        break
    test += 1


# user can see output of encrypted flag for each public exponent
c1 = pow(bytes_to_long(FLAG), e1, n)
c2 = pow(bytes_to_long(FLAG), e2, n)
c3 = pow(bytes_to_long(FLAG), e3, n)
c4 = pow(bytes_to_long(FLAG), e4, n)

# user get n_ans / public exponent
temp_1 = GCD(c1 - pow(c2, e1 // e2), c1 - pow(c3, e1 // e3))
n_ans = GCD(temp_1, c1 - pow(c4, e1 // e4))

print(n_ans)
print(n)
assert n_ans == n

# get flag
_, u, v = xgcd(e2, e3)
p1 = pow(c2, u, n) if u > 0 else pow(pow(c2, -1, n), -u, n_ans)
p2 = pow(c3, v, n) if v > 0 else pow(pow(c3, -1, n), -v, n_ans)
flag_ans = int(p1 * p2) % n_ans
print(long_to_bytes(flag_ans))

