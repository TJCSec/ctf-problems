#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int rands[5];
int nums[5];

void give_shell() {
  int i;
  for (i=0;i<5;++i) {
    if (nums[i] != rands[i]) {
      return;
    }
  }
  system("/bin/sh");
}

void f1() {
  nums[0] = rands[0];
}
void f2() {
  nums[1] = rands[1];
}
void f3() {
  nums[2] = rands[2];
}
void f4() {
  nums[3] = rands[3];
}
void f5() {
  nums[4] = rands[4];
}

char *name() {
  char buf[100];

  printf("Enter your name ");
  fflush(stdout);

  gets(buf);
  return buf;
}

int main(int argc, char **argv) {

  int seed = * (int *) argv[argc-1];
  srand(seed * 2942913);

  int i;
  for (i=0;i<5;++i) {
    rands[i] = rand();
  }

  char *n = name();
  printf("Your name is %s\n", n);
  give_shell();
}
