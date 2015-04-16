#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>

typedef struct P {
    char user[32];
    char pass[32];
    char mess[24];
    int canary;
    int authorized;
} Person;

void read_in(char buf[32]) {
    int i;
    char c;
    for (i = 0; i < 31; i++) {
        c = getchar();
        if (c == '\n' || c == EOF) {
            buf[i] = '\0';
            break;
        }
        buf[i] = c;
    }
    while (c != '\n' && c != EOF) c = getchar();
}

int main(int argc, const char* argv[]) {
    setbuf(stdout, NULL);
    
    Person* p = malloc(sizeof(Person));
    memset(p,0,sizeof(Person));
    
    struct timeval t1;
    gettimeofday(&t1, NULL);
    srand(t1.tv_usec * t1.tv_sec);
    int canary = rand();
    p->canary = canary;

    char user[128] = {0};
    char pass[128] = {0};
    FILE *f = fopen("credentials","r");
    fgets(user, sizeof(user), f);
    user[strlen(user)] = '\0';
    fgets(pass, sizeof(pass), f);
    pass[strlen(user)] = '\0';
    fclose(f);

    printf("Commands:\n"
           "\n"
           "u: Set username.\n"
           "p: Set password.\n"
           "m: Set message.\n"
           "d: Display info.\n"
           "c: Check authorization.\n"
           "f: If authorized, print flag.\n");

    char c;
    char c2;
    char buf[32] = {0};
    while (1) {
        printf(">");
        c = getchar();
        while ((c2 = getchar()) != '\n' && c2 != EOF);

        switch (c) {
            case 'u':
                printf("Enter new username.\n");
                read_in(buf);
                memcpy(p->user,buf,strlen(buf));
                break;
            case 'p':
                printf("Enter new password.\n");
                read_in(buf);
                memcpy(p->pass,buf,strlen(buf));
                break;
            case 'm':
                printf("Enter new message.\n");
                read_in(buf);
                memcpy(p->mess,buf,strlen(buf));
                break;
            case 'd':
                printf("User: %s\nPassword: %s\nMessage: %s\n",p->user,p->pass,p->mess);
                break;
            case 'c':
                if (!strncmp(user,p->user,32) && !strncmp(pass,p->pass,32)) {
                    p->authorized = 1;
                    printf("Valid credentials.\n");
                } else {
                    printf("Invalid credentials.\n");
                }
                break;
            case 'f':
                if (p->authorized) {
                    printf("Authorized!\nFlag: ");
                    FILE *f = fopen("flag","r");
                    while ((c2 = fgetc(f)) != EOF) {
                        printf("%c",c2);
                    }
                    fclose(f);
                } else {
                    printf("Not Authorized.\n");
                }
                break;
            default:
                printf("Invalid command.\n"
                       "Commands:\n"
                       "\n"
                       "u: Set username.\n"
                       "p: Set password.\n"
                       "m: Set message.\n"
                       "d: Display info.\n"
                       "c: Check authorization.\n"
                       "f: If authorized, print flag.\n\n");
        }
        if (canary != p->canary) {
            printf("Error: Canary has been changed.\n");
            return 1;
        }
    }
    return 0;
}
