#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/prctl.h>
#include <linux/audit.h>
#include <linux/filter.h>
#include <stddef.h>
#include <syscall.h>
#include <seccomp.h>

#define ulong unsigned long

void init() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);

    struct sock_filter filter[] = {
        BPF_STMT(BPF_LD | BPF_W | BPF_ABS, (offsetof(struct seccomp_data, nr))),

        BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K, __NR_execveat, 3, 0),
        BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K, __NR_execve, 2, 0),
        BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K, __NR_fork, 1, 0),

        BPF_STMT(BPF_RET | BPF_K, SECCOMP_RET_ALLOW),

        BPF_STMT(BPF_RET | BPF_K, SECCOMP_RET_KILL),
    };

    struct sock_fprog prog = {
        .len = sizeof(filter) / sizeof(struct sock_filter),
        .filter = filter,
    };

    if (prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0)) {
        perror("prctl(PR_SET_NO_NEW_PRIVS)");
        exit(-1);
    }

    if (syscall(SYS_seccomp, SECCOMP_SET_MODE_FILTER, 0, &prog)) {
        perror("seccomp");
        exit(-1);
    }
}

struct item {
    ulong price;
    char* name;
};

int N = 10, viewCount = 0;
struct item* items[10];
ulong itemNameSize[10];
int isAllocated[10];

ulong read_ulong() {
    char buf[0x20];
    read(0, buf, 16);
    return strtoul(buf, NULL, 10);
}

void add_item() {
    printf("At which slot? (0 - %d): ", N - 1);

    int idx;
    idx = read_ulong();
    if (idx < 0 || idx >= N) {
        puts("[❗] Sorry, you are not allowed to to that.");
        return;
    }

    printf("Item name size: ");
    itemNameSize[idx] = read_ulong();
    if (itemNameSize[idx] > 0x78) {
        puts("[❗] S-sorry, it's too long~ 😳");
        return;
    }

    items[idx] = malloc(sizeof(struct item));
    items[idx]->name = malloc(itemNameSize[idx]);

    printf("Item price: ");
    items[idx]->price = read_ulong();

    printf("Item name: ");
    read(0, items[idx]->name, itemNameSize[idx]);

    isAllocated[idx] = 1;
    puts("[✅] Item added successfully.");
}

void edit_item() {
    puts("[❗] Feature was deleted (yes, this is on purpose).");
}

void delete_item() {
    printf("At which slot? (0 - %d): ", N - 1);

    int idx;
    idx = read_ulong();
    if (idx < 0 || idx >= N || items[idx] == NULL) {
        puts("[❗] Sorry, you are not allowed to to that.");
        return;
    }

    free(items[idx]->name);
    free(items[idx]);
    isAllocated[idx] = 0;

    puts("[✅] Item deleted successfully.");
}

void view_item() {
    puts("[👀 - IMPORTANT] You can only view items twice!");
    printf("Remaining chance: %d.\n", 2 - viewCount);
    printf("\nAt which slot? (0 - %d): ", N - 1);

    int idx;
    idx = read_ulong();
    if (idx < 0 || idx >= N || !isAllocated[idx] || viewCount >= 2) {
        puts("[❗] Sorry, you are not allowed to to that.");
        return;
    }

    printf("Item price: %lu\n", items[idx]->price);
    printf("Item name: %s\n", items[idx]->name);
    viewCount++;

    puts("[✅] Item viewed successfully.");
}

int menu() {
    puts("");
    puts("=-=-=-=-= [COMPFEST Shop Sim v1.0.0 - MENU] =-=-=-=-=");
    puts("What do you want to do?");
    puts("1. Add item 😳");
    puts("2. Delete item 🗑️");
    puts("3. Edit item ✏️");
    puts("4. View item 👀");
    puts("5. Exit 😭");
    printf("> ");

    int choice;
    choice = read_ulong();
    return choice;
}

void introduction() {
    puts("???       : Umm hey! So, you must be the new worker here right? 😃");
    puts("???       : I\'m the manager here, nice to meet you. 😁");
    puts("Manager   : You\'re still new here, so I\'ll work you in our company's simulator first. 😊");
    puts("Manager   : Here you are in charge of managing the items in our shop.");
    puts("Manager   : You can add, delete, edit, and view items. But there are only 10 slots of items.");
    puts("Manager   : In order to make this a lot easier for you, there aren\'t any customers here yet to buy those items.");
    puts("Manager   : Well, isn\'t that great! You can learn how to manage items freely without any pressure!");
    puts("Manager   : Just make sure you don't do anything too unusual or, worse, accidentally break anything, okay? 😅");
    puts("Manager   : Well then, I must be going. Good luck, and most importantly, have some fun! 😉");
    puts("\n(📢) =-=-= Press [ENTER] to continue =-=-= (📢)");
    getchar();
    puts("Welcome to COMPFEST Shop Sim!");
    puts("Logged in as: [👨‍💼] New Worker");
}

int main() {
    init();
    introduction();

    while (69) {
        int choice = menu();
        switch (choice) {
            case 1:
                add_item();
                break;
            case 2:
                delete_item();
                break;
            case 3:
                edit_item();
                break;
            case 4:
                view_item();
                break;
            case 5:
                puts("[👋] Bye.");
                exit(0);
                break;
            default:
                puts("[❗] Invalid choice.");
                break;
        }
    }
}