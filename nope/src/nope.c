#include <stdio.h>
#include <stdlib.h>
#include <sys/ptrace.h>

// Might be a setuid binary
// or the password could be the flag

int main(int argc, const char* argv[])
{
    // needs asm antidebug trickery
    // may also need some other stuff to prevent a simple nopping out

    if (argc < 2) {
        printf("Usage: %s PASSWORD",argv[0]);
        return 0;
    }

    pid_t c = fork();

    if (c) {
        wait(NULL);
    } else {
        pid_t p = getppid();
        if (ptrace(PTRACE_ATTACH,p,0,0) < 0) {
            kill(p,15);
            printf("pls no\n");
            return 1; 
        }
        sleep(1);
        ptrace(PTRACE_DETACH,p,0,0);
        return 0;
    }

    if (getenv("LD_PRELOAD")) {
        printf("get rekt\n");
        return 1;
    }

    // replace 0 with some tricky password check
    // something like cnot from plaidctf, but not as hard
    if (0) {
        printf("Correct!\nFlag: ");
        FILE *f = fopen("flag","r");
        char c;
        while ((c = fgetc(f)) != EOF) {
            printf("%c",c);
        }
        fclose(f);
    } else {
        printf("Wrong password.\n");
    }
    return 0;
}
