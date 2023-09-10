# Working at COMPFEST Shop

by NeoZap

---

## Flag Mirror

```
COMPFEST15{Hello_heapnote_my_0ld_friend__I_ve_c0m3_to_pwn_y0u_4g41n_7f2aff1af5}
```

## Flag

```
COMPFEST15{hello_heapnote_my_old_friend__I_ve_c0me_to_pwn_y0u_4g41n_4aac84c7de}
```

## Description
You are a new and aspiring shop worker at COMPFEST Shop, a shop owned by COMPFEST Company. Upon arriving at the shop to begin your first day working, you met a mysterious figure. Looks like they want to say something to you, go on and listen to them!

`nc <ip> <port>`


## Difficulty
Tingkat kesulitan soal: hard

## Hints
> Intentionally left empty

## Tags
heap, uaf, house of spirit, tcache poisoning, safe linking, fsop, rop

## Deployment
- Install docker engine>=19.03.12 and docker-compose>=1.26.2.
- Run the container using:
```
docker-compose up --build --detach
```

## Notes
Pakai GLIBC 2.35 milik WSL Ubuntu 22.04 (ada safe linking protection).

**TODO: Make a better writeup i guess**
