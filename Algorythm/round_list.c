#include <stdio.h>
#include <stdlib.h>

typedef int element;
typedef struct ListNode
{
    element data;
    struct ListNode *link;
} ListNode;

void print_ilst(ListNode *head){
    ListNode *p;

    if (head == NULL) return;
    p = head->link;
    do{
        printf("%d->", p->data);
        p = p->link;
    } while (p != head);
    printf("%d->", p->data);
}

ListNode *insert_first(ListNode *head, element item){
    ListNode *node = (ListNode *)malloc(sizeof(ListNode));

    node->data = item;
    if(head == NULL){
        head = node;
        node->link = head; //원형구조로 생성된 리스트 이기때문에 다시 자기 자신으로 연결
    } else{
        node->link = head->link;
        head->link = node;
    }
    return head;
}

ListNode *insert_last(ListNode *head, element item){
    ListNode *node = (ListNode *)malloc(sizeof(ListNode));

    node->data = item;

    if(head == NULL){
        head = node;
        node->link = head;
    } else {
        node->link = head->link;
        head->link = node;
        head = node;
    }

    return head;
}

int main(void){
    ListNode *head = NULL;

    head = insert_last(head, 20);
    head = insert_last(head, 30);
    head = insert_last(head, 40);
    head = insert_first(head,10);
    head = insert_last(head, 50);
    print_ilst(head);

    return 0;
}
