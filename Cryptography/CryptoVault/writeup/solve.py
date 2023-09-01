import math
import ecdsa
import ecdsa.ellipticcurve as EC

def inv_mod_p(x, p):
    if 1 != math.gcd(x, p):
        raise ValueError("Arguments not prime")
    q11 = 1
    q22 = 1
    q12 = 0
    q21 = 0
    while p != 0:
        temp = p
        q = x // p
        p = x % p
        x = temp
        t21 = q21
        t22 = q22
        q21 = q11 - q*q21
        q22 = q12 - q*q22
        q11 = t21
        q12 = t22
    return q11

curve = ecdsa.SECP256k1
G = curve.generator
n = G.order()

#PUBKEY
x = int('ce205d44c14517ba33f3ef313e404537854d494e28fcf71615e5f51c9a459f42', 16)
y = int('6080e22d9a44a5ce38741f8994ac3a14a6760f06dd1510b89b6907dfd5932868', 16)
Q = EC.Point(curve.curve, x, y)
pubkey = ecdsa.VerifyingKey.from_public_point(Q, curve)

a = ecdsa.util.randrange(n-1)

valid_s = False
while not valid_s:
    b = ecdsa.util.randrange(n-1)
    b_inv = inv_mod_p(b, n)

    K = (a*G) + (b*Q)
    r = K.x() % n

    s = r * b_inv % n

    if 0 < s < n:
        valid_s = True

m = (((a * r) % n) * b_inv) % n

message_bytes32 = format(m, '064x')
r_bytes32 = format(r, '064x')
s_bytes32 = format(s, '064x')

print("message: " + message_bytes32)
print("r: " + r_bytes32)
print("s: " + s_bytes32)

sig = ecdsa.ecdsa.Signature(r, s)
if pubkey.pubkey.verifies(m, sig):
    print("COMPFEST15{dOnt_F0rgE7_t0_v3r1fy_7h3_m3s5Age}")
else:
    print("FAILED TO VERIFY")