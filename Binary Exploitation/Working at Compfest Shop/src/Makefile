all:
	gcc -o chall chall.c -fstack-protector-strong -D_FORTIFY_SOURCE=2 -Wformat -Wformat-security -pie -fPIE -Wl,-z,relro,-z,now
	cp chall ../public/chall
	pwninit --bin chall --no-template
clean:
	rm -f chall
	rm -f chall_patched
	rm -f ../public/chall
	rm -f libc.so.6
