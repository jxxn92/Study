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
ListNode *insert_first(ListNode *head, int item){

    ListNode *p = (ListNode *)malloc(sizeof(ListNode));
    p->name = "jun";
    p->link = head->link;
    head = p;
    
    return head;
}