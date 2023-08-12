//TODO 큐(QUEUE) : First In First Out

#include <stdio.h>
#include <stdlib.h>

#define MAX_QUEUE_SIZE 5

typedef int element;

typedef struct {
    int front;
    int rear;
    element data[MAX_QUEUE_SIZE];
} QueueType;

void init_queue(QueueType *q){
    q->front = 0;
    q->rear = 0;
}

void error(char *message){
    fprintf(stderr, "%s \n", message);
    exit(1);
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
    if (q->rear == MAX_QUEUE_SIZE){
        return 1;
    }
    else{
        return 0;
    }
}

void enqueue(QueueType *q, int item){
    if(is_full(q)){
        error("Stack Overflow");
    }
    q->data[++(q->rear)] = item;
}

element dequeue(QueueType *q){
    if(is_empty(q)){
        error("Stack is Empty");
    }
    else{
        return q->data[++(q->front)];
    }
}

void queue_print(QueueType *q){
    for (int i = 0; i < MAX_QUEUE_SIZE; i++){
        if(i <= q->front || i > q->rear){
            printf("  |  ");
        } else {
            printf(" %d  |  ");
        }
    }
    printf("\n");
}

int main(){
    QueueType q;
    init_queue(&q);

    enqueue(&q, 10); queue_print(&q);
    enqueue(&q, 20); queue_print(&q);
    enqueue(&q, 30); queue_print(&q);

    dequeue(&q); queue_print(&q);



}