# CryptoVault

by fahrul

---

## Flag

```
COMPFEST15{3CDSA_I5_7r1CKy_7O_IMPlEM3N7_85a7f9cdfe}
```

## Description

f0xie is building a vault to store his crypto wallet. He is using ECDSA as the authentication method since he recently learned ECDSA is super-secure. little did he know ECDSA implementation is super tricky. Can you break it? 

## Difficulty
Tingkat kesulitan soal: medium

## Hints
* Do you really need the web UI?
* Hmmm.... why the form and the api doesn't match?
* someone used this trick before to pretend to be someone else

## Tags
Crypto, ECDSA

## Deployment
Penjelasan cara menjalankan service yang dibutuhkan serta requirementsnya.

#### Cara 1
run main.py

#### Docker
    ```
    docker buildx build --tag my-image:latest .
    docker-compose up
    ```