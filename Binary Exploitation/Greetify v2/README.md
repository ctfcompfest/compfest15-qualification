# Greetify v2

by NeoZap

---

## Flag Mirror

```
COMPFEST15{NoOOoo0O00O0___th3_w0rld_st1ll_need_more_w4rm_gr333tingszzz_ccec571261}
```

## Flag

```
COMPFEST15{NoOOoo0O0O0___th3_w0rld_st1ll_need_more_w4rm_gr333tingszzz_18eb4c0c9d}
```

## Description
Because I'm feeling lonely, I created an application to greet me once again. However, I realized that I'm not the only one who is feeling lonely, so I modified it to be able to greet anyone. Nevertheless, I'm unsure about its safety. Could you please help me check it?

**P.S: Due to limitations on my server, each session is restricted to a duration of 5 seconds ☹️ (to simulate this behavior, run the binary with this command: `timeout 5 ./chall`)**

`nc <ip> <port>`

## Difficulty
Tingkat kesulitan soal: easy-medium

## Hints
> Intentionally left empty

## Tags
one-byte stack overflow, format string, libc database, one gadget

## Deployment
- Install docker engine>=19.03.12 and docker-compose>=1.26.2.
- Run the container using:
```
docker-compose up --build --detach
```

## Notes
- Libc gausah dikasih
- Hackerclass kasih soal yang lookup libc sendiri, biar peserta ga kaget(?)
