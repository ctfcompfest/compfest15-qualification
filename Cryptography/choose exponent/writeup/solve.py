from sage.all import *
from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime, GCD
from pwn import remote

# FLAG = b"COMPFEST15{REDACTED}".ljust(256, b"\x00")

# test = 0
# while True:
#     # all parameter not publicly known
#     p = getPrime(1024)
#     q = getPrime(1024)
#     n = p * q
#     phi = (p - 1) * (q - 1)

#     # user can input max 3 public exponent
#     e1 = 3
#     e2 = 5
#     e3 = e1 * e2
#     print("gcd", GCD(e3, phi))
#     # if GCD(e3, phi) == 1:
#     #     print(test)
#     #     print(n, "n")
#     #     break
#     break


# # user can see output of encrypted flag for each public exponent
# c1 = pow(bytes_to_long(FLAG), e1, n)
# c2 = pow(bytes_to_long(FLAG), e2, n)
# c3 = pow(bytes_to_long(FLAG), e3, n)

# # user get n_ans / public exponent
# n_ans = GCD(c3 - pow(c2, e3 // e2), c3 - pow(c1, e3 // e1))
# # n_ans = GCD(temp_1, c1 - pow(c3, e1 // e2))
# print(n, "n")
# print(n_ans, "n_ans")


# #get flag
# _, u, v = xgcd(e1, e2)
# p1 = pow(c1, u, n_ans)
# p2 = pow(c2, v, n_ans)
# flag_ans = int(p1 * p2) % n_ans
# print(long_to_bytes(flag_ans))

def io():
    return remote("localhost", 9999)

def get_encrypted_flag(r, e):
    r.recvuntil(b">> ")
    r.sendline(b"1")
    r.recvuntil(b"Enter your public exponent (e cannot be 1 and even): ")
    r.sendline(str(e).encode())
    r.recvuntil(b"Here is your encrypted flag: ")
    return int(r.recvline().strip())

while True:
    try:
        r = io()

        e1 = 3
        e2 = 5
        e3 = e1 * e2

        c1 = get_encrypted_flag(r, e1)
        c2 = get_encrypted_flag(r, e2)
        c3 = get_encrypted_flag(r, e3)

        n = GCD(c3 - pow(c2, e3 // e2), c3 - pow(c1, e3 // e1))
        _, u, v = xgcd(e1, e2)
        p1 = pow(c1, u, n)
        p2 = pow(c2, v, n)
        flag = long_to_bytes(int(p1 * p2) % n)
        if b"COMPFEST" in flag:
            print(flag.strip(b"\x00").decode())
            break
    except:
        pass
    r.close()




