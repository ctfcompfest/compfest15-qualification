# hackedlol

by k3ng

---

## Flag

```
COMPFEST15{b1G_brr41nz_ us1ng_c0d3_4s_k3y_0a53f5b9a3}
```

## Description
Someone hacked my computer! I really need my important file but it's encrypted. The IT guy managed to recover one file. But I don’t think that is my file though.

## Difficulty
easy

## Hints
* hint 1
* hint 2
* hint dst.

## Tags
Python Bytecode, Obfuscation

## Deployment
Penjelasan cara menjalankan service yang dibutuhkan serta requirementsnya.

#### Contoh 1
- Install docker engine>=19.03.12 and docker-compose>=1.26.2.
- Run the container using:
    ```
    docker-compose up --build --detach
    ```

#### Contoh 2
- How to compile:
    ```
    gcc soal.c -o soal -O2 -D\_FORTIFY\_SOURCE=2 -fstack-protector-all -Wl,-z,now,-z,relro -Wall -no-pie
    ```
- Jalankan:
    ```
    ./soal
    ```
- Workdir di `/home/compfest14`
- Gunakan libc 2.31 ketika sudah keluar. Alias Ubuntu 20.04.

## Notes
Tambahan informasi untuk soal, deployment, atau serangan yang mungkin terjadi pada service soal
