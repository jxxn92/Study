#include <stdio.h>
#include <stdlib.h>

typedef int element;

typedef struct ListNode{
    element data;
    struct ListNode *link;
} ListNode;

ListNode *insert_first(ListNode * head, element value){

    ListNode *p = (ListNode *)malloc(sizeof(ListNode));

    p->data = value;
    p->link = head;
    head = p;

    return head;
}

void print_list(ListNode *head){

    for(ListNode *p = head; p != NULL; p = p->link)
        printf("%d ->", p->data);
    printf("NULL \n");
}

ListNode *reverse(ListNode *head){
    // 순회 포인터로 p, q, r 사용
    ListNode *p, *q, *r;

    p = head;
    q = NULL;

    while (p != NULL){

        r = q; 
        q = p; // q가 데이터
        p = p->link;
        q ->link = r;
    }
    return q;
}

int main(void){

    ListNode *head1 = NULL;
    ListNode *head2 = NULL;

    head1 = insert_first(head1, 1);
    head1 = insert_first(head1, 2);
    head1 = insert_first(head1, 3);
    print_list(head1);

    head2 = reverse(head1);
    print_list(head2);

    return 0;
}