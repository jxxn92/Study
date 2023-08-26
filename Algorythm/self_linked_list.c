#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100

typedef int element;

typedef struct ListNode{
    element data;
    struct ListNode *link;
} ListNode;

void error(char *message){
    fprintf(stderr, "%s\n", message);
    exit(1);
}

ListNode *insert_first(ListNode *head, int item){

    ListNode *p = (ListNode *)malloc(sizeof(ListNode));
    p->data = item;
    p->link = head->link;
    head = p;
    
    return head;
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

ListNode *insert(ListNode *head, ListNode *pre, int item){

    ListNode *p = (ListNode *)malloc(sizeof(ListNode));
    p->data = item;
    p->link = pre->link;
    pre->link = p;

    return head;
}

ListNode *delete_first(ListNode *head){
    
    ListNode *remove;
    if (head == NULL) return NULL;
    remove = head;
    head = remove->link;
    free(remove);

    return head;
    
}

ListNode *delete_last(ListNode *head){

    ListNode *remove;
    ListNode *prev;
    prev = head;
    if(head == NULL) return NULL;

    while(prev->link->link != NULL)
        prev = prev->link;
    prev->link = NULL;

    return head;

}

ListNode *delete(ListNode *head, ListNode *pre){

    ListNode *remove;
    remove = pre->link;
    pre->link = remove->link;
    free(remove);

    return head;

}

ListNode *search_list(ListNode *head, element x){

    ListNode *p = head;

    while(p != NULL){
        if(p->data == x)
            return p;
        p = p->link;
    }
    return NULL;
}

ListNode *sum_list(ListNode *head){

    int s = 0;

    for(ListNode *p = head; p != NULL; p = p->link){
        s += p->data;
    }
    return s;
}

void print_list(ListNode *head){

    for(ListNode *p = head; p != NULL; p=p->link){
        printf("%d->",p->data);
    }
    printf("NULL \n");
}

ListNode *find_max(ListNode *head){
    int max_num = head->data;
    for(ListNode *p = head; p != NULL; p=p->link){
        if(p->data >= max_num)
            max_num = p->data;
    }
    return max_num;
}

ListNode *find_min(ListNode *head){
    int min_num = head->data;
    for(ListNode *p = head; p != NULL; p = p->link){
        if(p->data <= min_num)
            min_num = p->data;
    }
    return min_num;
}

int main(void){

    ListNode *head = NULL;

    head = insert_first(head, 1);    
    print_list(head);
    head = insert_first(head, 2);    
    print_list(head);
    head = insert_first(head, 3);    
    print_list(head);
    head = insert_last(head, 10);    
    print_list(head);
    head = insert_last(head, 30);    
    print_list(head);
    
    return 0;
}