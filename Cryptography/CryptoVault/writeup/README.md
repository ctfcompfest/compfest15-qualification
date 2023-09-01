# Writeup

ECDSA signatures where the message isn't a hash and chosen by the "signer" are insecure.

Given public key P, pick random nonzero values a and b. Compute R=aG+bP. Now (R.x, R.x/b) is a valid signature for "message" (R.x*a/b).

https://twitter.com/pwuille/status/1063582706288586752

script on solve.py