#include <stdio.h>
#include <stdlib.h>

typedef int element;

typedef struct DListNode {
    element deta;
    struct DListNode *head;
    struct DListNode *tail;
} DListNode;

void init(DListNode *phead){
    phead->head = phead;
    phead->tail = phead;
}

void print_dlist(DListNode *phead){
    DListNode *p;

    for(p = phead->tail; p != phead; p = p->tail){
        printf("<-| |%d| |->",p->deta);
    }
    printf("\n");
}

void dinsert(DListNode *before, element item){
    
    DListNode *new = (DListNode *)malloc(sizeof(DListNode));
    new->deta = item;
    new->head = before;
    new->tail = before->tail;
    before->tail->head = new;
    before->tail = new;

}

void ddelete(DListNode *head, DListNode* removed){
    if (head == NULL) return;
    removed->tail->head = removed->head;
    removed->head->tail = removed->tail;
    free(removed);
}

int main(void){
    DListNode *head = (DListNode *)malloc(sizeof(DListNode));
    init(head);
    printf("추가 단계\n");
    for(int i = 0; i < 5; i++){
        dinsert(head, i);
        print_dlist(head);
    }

    printf("삭제 단계\n");
    for(int i = 0; i < 5; i++){
        ddelete(head,head->tail);
        print_dlist(head);
    }
    free(head);

    return 0;
}

