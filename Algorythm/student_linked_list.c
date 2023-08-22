#include <stdio.h>
#include <stdlib.h>

typedef int element;
typedef struct ListNode{
    char *name;
    int age;
    double height;
    struct ListNode *link;
} ListNode;

void error(char *message){
    fprintf(stderr, "%s \n", message);
    exit(1);
}