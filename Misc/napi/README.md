# napi

by k3ng

---

## Flag

```
COMPFEST15{clo5e_y0ur_f1LE_0bj3ctS_plZzz___THXx!!!_63bf937957}
```

## Description
john is currently planning an escape from jail.
Fortunately, he got a snippet of the jail source code from his cellmate.
Can you help john to escape?

## Difficulty
Tingkat kesulitan soal: easy

## Hints
* Someone told me that the admin can still log in from here. So the admin login is still Functional. Just not the usual way.

## Tags
Python Jail

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
```
SSH Port: 6969
Netcat Port: 4321
```
