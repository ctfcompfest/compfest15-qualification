#!/bin/sh

/usr/sbin/sshd
socat TCP-LISTEN:9999,fork EXEC:'/usr/bin/python3 chall.py'