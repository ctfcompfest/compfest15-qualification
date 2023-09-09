from sage.all import *
from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime, GCD
from pwn import remote

def io():
    return remote("localhost", 10004)

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
    except Exception as e:
        print(e)
        pass

    r.close()




