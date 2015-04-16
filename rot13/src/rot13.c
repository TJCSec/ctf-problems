#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>

// gcc's variable reordering messes with this problem
char tmp[256] = {0};
int end = 0;
int size = 0;

int rotinput(char* t, int size) {
    int i;
    int c;
    for (i = 0; i < size-1; i++) {
        c = getchar();

        if (c == '\n' || c == EOF) {
            if (c == '\n') {
                t[i] = '\n';
                i++;
            }
            t[i] = 0;
            break;
        }

        if ((c >= 'a' && c < 'a'+13) || (c >= 'A' && c < 'A'+13)) {
            c += 26;
        }

        c -= 13;
        t[i] = c;
    }

    return i;
}

void handle_signal(int signum) {
    if (signum == SIGHUP)
        exit(0);
}

int main() {
    setbuf(stdout, NULL);
    signal(SIGHUP, handle_signal);
    
    char buf[256] = {0};
    printf("ROT13-ATOR\n");
    printf("Input strings. Send an empty newline to end.\n");
    while (strcmp(tmp,"\n")) {
        memset(tmp, 0, 256);
        size = rotinput(tmp, 256);
        if (strlen(tmp) + strlen(buf) < 256) {
            memcpy(buf + end, tmp, size);
            end += strlen(tmp);
        } else {
            printf("Buffer is full, ending.\n");
            break;
        }
    }
    printf("%s\n",buf);
}
