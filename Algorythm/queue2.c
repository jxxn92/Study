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
    fprintf(stderr, "%s \n", message);
    exit(1);
}

void init_queue(QueueType *q){
    q->front = -1;
    q->rear = -1;
}

void print_queue(QueueType *q){
    for(int i = 0; i < MAX_SIZE; i++){
        if (i <= q->front || i > q->rear){
            printf(" | ");
        } else{
            printf(" %d | ", q->data[i]);
        }
    }
    printf("\n");
}

int is_empty(QueueType *q){
    if(q->front == q->rear){
        return 1;
    }
    else{
        return 0;
    }
}

int is_full(QueueType *q){
    if(q->rear == (MAX_SIZE-1)){
        return 1;
    }
    else{
        return 0;
    }
}

void enqueue(QueueType *q, element item){
    if(is_full(q)){
        error("Stack Overflow");
    }
    else{
        q->data[++(q->rear)] = item;
    }
}

element dequeue(QueueType *q){
    if(is_empty(q)){
        error("Stack is Empty");
    }
    else{
        return q->data[++(q->front)];
    }
}

int main(void){

    QueueType q;
    init_queue(&q);

    enqueue(&q, 1); print_queue(&q);
    enqueue(&q, 2); print_queue(&q);
    enqueue(&q, 3); print_queue(&q);

    dequeue(&q); print_queue(&q);
    dequeue(&q); print_queue(&q);
    dequeue(&q); print_queue(&q);
}