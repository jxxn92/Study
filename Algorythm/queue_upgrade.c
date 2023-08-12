#include <stdio.h>
#include <stdlib.h>
#define MAX_SIZE 5

typedef int element;

typedef struct {
    int front;
    int rear;
    element data[MAX_SIZE];
} QueueType;


void init_queue(QueueType *q){
    q->front = 0;
    q->rear = 0;
}

int is_empty(QueueType *q){
    return (q->front == q->rear);
}

int is_full(QueueType *q){
    return ((q->rear+1) % MAX_SIZE == q->front);
}

void error(char *message){
    fprintf(stderr, "%s \n", message);
    exit(1);
}

void print_queue(QueueType *q){
    printf("QUEUE(front=%d rear=%d) = ", q->front, q->rear);
    if(!is_empty(q)){
        int i = q->front;
        do{
            i = (i+1) % MAX_SIZE;
            printf(" %d | ",q->data[i]);
            if (i == q->rear){
                break;
            }
        } while(i != q->front);
    }
    printf("\n");
}

void add_front(QueueType *q, element item){
    if(is_full(q)){
        error("Stack Overflow");
    }
    q->data[q->front] = item;
    q->front = (q->front - 1 + MAX_SIZE) % MAX_SIZE;
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

element delete_rear(QueueType *q){
    int prev = q->rear;
    if(is_empty(q)){
        error("Stack is Empty");
    }
    q->rear = (q->rear - 1 + MAX_SIZE) % MAX_SIZE;
    return q->data[prev];
}

int main(void){
    QueueType q;

    init_queue(&q);

    for (int i = 0; i < 3; i++){
        add_front(&q,i); print_queue(&q);
    }
    for (int i = 0; i < 3; i++){
        delete_rear(&q); print_queue(&q);
    }

    return 0;
}