#include <stdio.h>
#include <string.h>
#include <unistd.h>

#define buf_size 2*16+8+1

void init() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

void name_error() {
    printf("\nI'm not sure if I can spell your name...");

    __asm__ volatile ("mov $60, %rax;"
        "xor %rdi, %rdi;"
        "syscall");
}

void readnline(char* buf, size_t n) {
    for (int i = 0; i <= n; ++i) {
        char x;
        int chk = read(0, &buf[i], 1);
        if (chk <= 0) {
            name_error();
        }
        if ((x = buf[i]) == '\n') {
            buf[i] = '\0';
            return;
        }
    }
}

void check(char* buf) {
    int len = strlen(buf);
    if (len > 9) {
        printf("Your name is too long, so..");
        name_error();
    }
    for (int i = 0; i < len; i++) {
        if (buf[i] < ' ' || buf[i] > '~') {
            name_error();
        }
    }
}

int main() {
    init();
    printf("\nWelcome to Greetify v2! ^^\nWe are here to greet you, hope you enjoy our company! :D");
    printf("\nFirst off, what is your name? ");

    char buf[buf_size - 1];
    readnline(buf, buf_size - 1);
    check(buf);

    printf("\nHello, ");
    printf(buf);
    printf("!👋\nBye bye, please come back if you are lonely, we are always here for you! :D");
}
