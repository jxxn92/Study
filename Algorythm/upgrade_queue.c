/*
* 일단 필요한 기능들을 구현 해야합니다.
* 1. error v
* 2. empty v
* 3. full v
* + init v
* 4. add_front v
* 5. add_rear v
* 6. delete_front v
* 7. delete_rear v
* 8. get_front
* 9. get_rear
* 10. print
*/
#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 5

typedef int element;

typedef struct {
    int front;
    int rear;
    element data[MAX_SIZE];
} QueueType;

void error(char *message){
    fprintf(stderr, "%s\n", message);
    exit(1);
}

void init_queue(QueueType *q){
    q->front = 0;
    q->rear = 0;
}

int is_empty(QueueType *q){
    return (q->front == q->rear);
}

int is_full(QueueType *q){
    return ((q->rear + 1) % MAX_SIZE == q->front);
}

void add_rear(QueueType *q, element item){
    if(is_full(q)){
        error("Stack Overflow");
    }
    q->rear = (q->rear + 1) % MAX_SIZE;
    q->data[q->rear] = item;
}

element delete_front(QueueType *q){
    if(is_empty(q)){
        error("Stack is Empty");
    }
    q->front = (q->front + 1) % MAX_SIZE;
    return q->data[q->front];     
}

void add_front(QueueType *q, element item){
    if(is_full(q)){
        error("Stack Overflow");
    }
    q->data[q->front] = item;
    q->front = (q->front - 1 + MAX_SIZE) % MAX_SIZE;
}

element delete_rear(QueueType *q){
    if(is_empty(q)){
        error("Stack is Empty");
    }
    int val = q->rear;
    q->rear = (q->rear - 1 + MAX_SIZE) % MAX_SIZE;
    return q->data[val];
}

element get_rear(QueueType *q){
    if(is_empty(q)){
        error("Stack is Empty");
    }
    return q->data[q->rear];
}

element get_front(QueueType *q){
    if(is_empty(q)){
        error("Stack is Empty");
    }
    return q->data[(q->front + 1) % MAX_SIZE];
}

void print_queue(QueueType *q){
    printf("QUEUE(front=%d rear=%d) = ", q->front, q->rear);
    if(!is_empty(q)){
        int i = q->front;
        do {
            i = (i + 1) % MAX_SIZE;
            printf("%d | ", q->data[i]);
            if(i == q->rear)
                break;
        } while (i != q->front);
    }
    printf("\n");
}

int main(void){
    
    QueueType q;

    init_queue(&q);

    for(int i = 0; i < 3; i++){
        add_front(&q, i);
        print_queue(&q);
    }

    for(int i = 0; i < 3; i++){
        delete_rear(&q);
        print_queue(&q);
    }
    return 0;
}
