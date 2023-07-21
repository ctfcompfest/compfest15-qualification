# artificial secret

by fahrul

---

## Flag

```
COMPFEST15{d0nT_STOR3_S3CrET_On_Pr0MP7_874131ddff}
```

## Description

I'm developing an AI Waifu chatbot startup but i'm too lazy to host my own LLMs, So i just use chatGPT API, but first i need to hide my prompt since it's my only moat, can you help me pentesting this? 

the bot is online as `lemond
#8498` on the Discord server, but only talking in DMs. 
(Note: this challenge requires no automation. Please do not automate your Discord account as that is a violation of Discord's Terms of Service and may lead to the termination of your account)


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