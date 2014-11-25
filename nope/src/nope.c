#include <stdio.h>
#include <stdlib.h>
#include <sys/ptrace.h>

// Might be a setuid binary
// or the password could be the flag

int a = 0;

void anti_debug() {
    // if someone nops out the call for this, the password changes
    a += 15;
    if (getenv("LD_PRELOAD")) {
        printf("nope");
        exit(0);
    }
    a += 30;
}

int main(int argc, const char* argv[])
{
    // needs asm antidebug trickery
    // may also need some other stuff to prevent a simple nopping out

    anti_debug(); // honeypot 

    pid_t c = fork();

    if (c) {
        a += 15;
        wait(NULL);
    } else {
        pid_t p = getppid();
        if (ptrace(PTRACE_ATTACH,p,0,0) < 0) {
            kill(p,15);
            printf("pls go\n");
            return 1; 
        }
        sleep(1);
        ptrace(PTRACE_DETACH,p,0,0);
        return 0;
    }

    a += 30;
    if (getenv("LD_PRELOAD")) {
        printf("get rekt\n");
        return 1;
    }

    if (argc < 2) {
        printf("Usage: %s FLAG\n",argv[0]);
        return 0;
    }

    // replace 0 with some tricky password check
    // something like cnot from plaidctf, but not as hard
    // also use the value of a
    if (0) {
        printf("Correct!\nFlag: %s",argv[1]);
    } else {
        printf("Wrong password.\n");
    }
    return 0;
}
