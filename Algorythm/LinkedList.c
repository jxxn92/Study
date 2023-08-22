#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100
typedef int element;

typedef struct ListNode
{
    element data;
    struct ListNode *link;
} ListNode;

void error(char *message){
    fprintf(stderr, "%s\n", message);
    exit(1);
}

ListNode* insert_first(ListNode* head, int item){

    ListNode *p = (ListNode *)malloc(sizeof(ListNode));
    p->data = item;
    p->link = head;
    head = p;
    
    return head;
}

ListNode *insert(ListNode* head, ListNode* pre, int item){

    ListNode *p = (ListNode *)malloc(sizeof(ListNode));
    p->data = item;
    p->link = pre->link;
    pre->link = p;

    return head;
}

ListNode *search_list(ListNode *head, element x){

    ListNode *p = head;

    while (p!= NULL)
    {
        if (p->data == x) return p;
        p = p ->link;
    }
    return NULL;
}

ListNode *delete_first(ListNode* head){

    ListNode *remove;
    if (head == NULL) return NULL;
    remove = head;
    head = remove->link;
    free(remove);

    return head;   
}

ListNode *delete(ListNode *head, ListNode *pre){

    ListNode *remove;
    remove = pre->link;
    pre->link = remove->link;
    free(remove);

    return head;
}

void print_list(ListNode *head){

    for(ListNode *p = head; p != NULL; p = p->link){
        printf("%d->",p->data);
    }
    printf("NULL \n");
}

ListNode *insert_last(ListNode *head, int item){

    ListNode *p = (ListNode *)malloc(sizeof(ListNode));
    ListNode *prev = head;

    p->data = item;
    p->link = NULL;

    while (prev->link != NULL) 
        prev = prev->link; // 끝 노드 도착인데.. 사실상
    prev->link = p;

    return head;

}

ListNode *sum_list(ListNode *head){

    int s = 0;

    for(ListNode *p = head; p != NULL; p = p->link){
        s += p->data;
    }
    return s;
}
int main(void){

    ListNode *head = NULL;

    for(int i = 0; i < 5; i++){
        head = insert_first(head, i);
        print_list(head);
    }
    for(int i = 10; i < 15; i++){
        head = insert_last(head, i);
        print_list(head);
    }
    int sum = sum_list(head);
    printf("%d",sum);
    // for(int i = 0; i < 5; i++){
    //     head = delete_last(head);
    //     print_list(head);
    // }

    return 0;
}