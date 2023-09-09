# industrialspy

by k3ng

---

## Flag

```
COMPFEST15{m0D3rn_D4y_5p1es_cb06cc3651}
MIRROR: COMPFEST15{b4cKgR0unD_Ch3CK_uR_1nT3rnS_cff5ca334b}
```

## Description
Dear IT guy,
I have suspicions that our graphic designer intern is stealing confidential documents and
sending them to our competitor. I have sent her PC's memory dump to analyze.

https://drive.google.com/file/d/18u8OSCejwV5Wo7Ezh7NLlVpuhkMQbw4d/view?usp=sharing

MIRROR: https://drive.google.com/file/d/1923XC_EyweYVt_8CsE9Luysq2njkfBN3/view?usp=sharing

## Difficulty
easy

## Hints
* hint 1
* hint 2
* hint dst.

## Tags
Tags dari soal pisahkan koma (e.g: tags1, tags2, tags3)

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
