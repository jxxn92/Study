#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef char element[100];

typedef struct DListNode
{
    element data;
    struct DListNode *head;
    struct DListNode *tail;
} DListNode;

DListNode *current;

void init(DListNode *phead){
    phead->head = phead;
    phead->tail = phead;
}

void print_dlist(DListNode *phead){
    DListNode *p;
    for(p = phead->tail; p != phead ;p = p->tail){
        if(p == current)
            printf("<-| | #%s# | |->",p->data);
        else
            printf("<-| | %s | |->",p->data);
    }
    printf("\n");
}

void dinsert(DListNode *before, element item){
    DListNode *new = (DListNode *)malloc(sizeof(DListNode));

    strcpy(new->data,item);
    new->head = before;
    new->tail = before->tail;
    before->tail->head = new;
    before->tail = new;

}

void ddelete(DListNode *head, DListNode *removed){
    if(removed == NULL) return;
    removed->tail->head = removed->head;
    removed->head->tail = removed->tail;

    free(removed);
}

int main(void){
    char ch;
    DListNode *head = (DListNode *)malloc(sizeof(DListNode));
    init(head);

    dinsert(head, "Mamamia");
    dinsert(head, "Dancing Queen");
    dinsert(head, "Fernando");

    current = head->tail;
    print_dlist(head);

    do{
        printf("명령어를 입력하시오(<, >, q): ");
        ch = getchar();
        if(ch == '<'){
            current = current->head;
            if (current == head)
                current = current->head;
        }
        else if (ch == '>'){
            current = current->tail;
            if (current == head) 
                current = current->tail;
        }
        print_dlist(head);
        getchar();
    } while (ch != 'q');

}