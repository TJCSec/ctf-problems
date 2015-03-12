#include <stdlib.h>
#include <stdio.h>
#include <string.h>

struct node {
    struct node* next;
    struct node* last;
    char value;
};

char stack[1024];
int stack_index;
int solution[] = { 2, 3, 40, 8, 13, 0, 46, 13, 0, 23, 10, 49, 2, 46 };

struct node* make_node(char* str, int arg) {
    struct node* head = malloc(sizeof(struct node));
    struct node* old = head;
    struct node* prev;

    int count = 0;
    int len = strlen(str);

    while(count < len) {
        head->next = malloc(sizeof(struct node));
        head->value = *str;
        prev = head;
        head = head->next;
        str += arg;
        count += arg;
        arg++;
    }

    head->value = 0;
    old->last = prev;
    return old;
}

int check(struct node* n, char* c) {
    int flag = 0;
    while(n->value) {
        if(n->value==32) break;
        if(*c) {
            if(n->value == *c) {
                flag = 1;
            }
            else {
                flag = 0;
            }
        }
        else {
            return 0;
        }
        n = n->next;
        c++;
    }
    return flag;
}

char* sol(char* c) {
    int i = 0;
    char* result = malloc(sizeof(char) * 64);
    for(i = 0; i < sizeof(solution) / sizeof(int); i++) {
        result[i] = c[solution[i]];
    }
    result[i + 1] = 0;
    return result;
}

void push(char s) { stack[stack_index++] = s; }
char pop() { return stack[--stack_index]; }

int main() {
    struct node* one = make_node("memory_corruption!", 1);
    struct node* two = make_node("buffer_overflow!", 2);
    struct node* three = make_node("return_oriented_programming!", 3);
    struct node* four = make_node("do_you_remember_picoctf?", 4);
    struct node* five = make_node("baleful_was_my_favorite_problem", 5);
    struct node* six = make_node("not_a_forensice_challenge", 6);
    struct node* seven = make_node("your_flag_is_just_kidding_there_is_no_flag_here", 7);
    struct node* eight = make_node("did_you_know_that_ctf_is_more_fun_with_mips_assembly", 8);
    struct node* nine = make_node("lorem_ipsum_dolor_sit_amet_consecutor_idk_what_goes_here", 9);
    struct node* ten = make_node("lolnothingtoseehere", 0);
    struct node* eleven = make_node("gosh_are_you_really_still_reading_these", 14);
    struct node* twelve = make_node("k...", 1);
    struct node* meme = make_node("y u no play moar vvvvry spooky game", 2);
    struct node* c = make_node("c is my favorite language", 4);
    two->last->next = three;
    three->last->next = five;
    five->last->next = four;
    four->last->next = nine;
    nine->last->next = one;
    one->last->next = ten;
    ten->last->next = twelve;
    twelve->last->next = eleven;
    eleven->last->next = meme;
    meme->next = c;

    char result[256];
    scanf("%s", &result);
    printf("%s\n", result);
    if(check(two, result))
        printf("%s\n", sol(result));
}
