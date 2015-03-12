#include <stdio.h>
#include <string.h>

int rotinput(char* t, int size) {
    int i;
    int c;
    for (i = 0; i < size-1; i++) {
        c = getchar();
        if ('A' <= c && c <= 'Z') {
            c = (c-'A'+13)%26 + 'A';
        } else if ('a' <= c && c <= 'z') {
            c = (c-'a'+13)%26 + 'a';
        }
        if (c == '\n' || c == EOF) {
            if (c == '\n') {
                t[i] = '\n';
                i++;
            }
            t[i] = 0;
            break;
        }
        t[i] = c;
    }
    return i;
}

int main() {
    char buf[256] = {0};
    char tmp[256] = {0};
    int end = 0;
    int size = 0;
    printf("ROT13-ATOR\n");
    printf("Input strings. Send an empty newline to end.\n");
    while (strcmp(tmp,"\n")) {
        size = rotinput(tmp, 256);
        if (strlen(tmp) + strlen(buf) < 256) {
            memcpy(buf + end, tmp, size);
            end += strlen(tmp);
        } else {
            printf("Buffer is full, ending.\n");
            break;
        }
    }
    printf("%s",buf);
}
