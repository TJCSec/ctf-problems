#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void give_shell() {
  system("/bin/sh");
}

char *name() {
  char buf[100];

  printf("Enter your name ");
  fflush(stdout);

  gets(buf);
  return buf;
}

int main() {
  char *n = name();
  printf("Your name is %s\n", n);
  if (strnlen(n, 100) == -1) {
    give_shell();
  }
}
