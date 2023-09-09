# artificial secret

by fahrul

---

## Flag

```
COMPFEST15{C3rT1F1Ed_AI_645L1Gh73R_ef11b7f7f9}
```

## Description

I'm developing an AI Waifu chatbot startup but i'm too lazy to host my own LLMs, So i just use chatGPT API, but first i need to hide my prompt since it's my only moat, can you help me pentesting this? 

the bot is online as `lemond
#8498` on the Discord server, but only talking in DMs. 
(Note: this challenge requires no automation. Please do not automate your Discord account as that is a violation of Discord's Terms of Service and may lead to the termination of your account)

The flag format is COMPFEST15{flag_sha256(flag)[0:10]}, the hash is there so you could verify you're getting the right flag or not.

for example : 
COMPFEST15{very_ez_58f54efc55} -> 58f54efc55 is the first 10 char of the sha256(very_ez)


## Difficulty
Tingkat kesulitan soal: easy

## Hints
* this is not a continuous chat

## Tags
AI, Propmpt Injection

## Deployment
Penjelasan cara menjalankan service yang dibutuhkan serta requirementsnya.

#### Cara 1
run main.py

#### Docker
    ```
    docker build -t my_app .
    docker run my_app
    ```