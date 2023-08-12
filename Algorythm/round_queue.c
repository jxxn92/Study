#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 6

typedef int element;

typedef struct {
    int rear; // 값 추가할 때 증가
    int front; // 값 삭제 할때 증가
    element data[MAX_SIZE];
} RQueueType;

void error(char *message){
    fprintf(stderr, "%s \n", message);
    exit(1);
}


void init_queue(RQueueType *r){
    r->front = 0;
    r->rear = 0;
}

int is_empty(RQueueType *r){
    if(r->rear == r->front){
        return 1;
    }
    else{
        return 0;
    }
}

int is_full(RQueueType *r){
    if((r->rear+1) % MAX_SIZE == r->front){
        return 1;
    }
    else{
        return 0;
    }
}


void print_queue(RQueueType *r){
    printf("QUEUE(front=%d rear=%d) = ", r->front, r->rear);
    if(!is_empty(r)){
        int i = r->front;
        do{
            i = (i+1) % MAX_SIZE;
            printf(" %d | ",r->data[i]);
            if (i == r->rear){
                break;
            }
        } while(i != r->front);
    }
    printf("\n");
}

void enqueue(RQueueType *r, element item){
    if(is_full(r)){
        error("QUEUE Overflow");
    }
    else{
        r->rear = (r->rear + 1) % MAX_SIZE;
        r->data[r->rear] = item;
    }   
}

element dequeue(RQueueType *r){
    if(is_empty(r)){
        error("QUEUE is Empty");
    }
    else{
        r->front = (r->front + 1) % MAX_SIZE;
        return r->data[r->front];
    }
}

element peek(RQueueType *r){
    if(is_empty(r)){
        error("QUEUE is Empty");
    }
    else{
        return r->data[(r->front +1) % MAX_SIZE];
    }
}

int main(void){
    
    RQueueType r;
    int element;
    init_queue(&r);

    printf("-- 데이터 추가 단계 --\n");
    while (!is_full(&r))
    {
        printf("정수를 입력하세요 : ");
        scanf("%d", &element);
        enqueue(&r, element);
        print_queue(&r);
    }
    printf("큐가 포화상태입니다.");

    printf("-- 데이터 삭제 단계 --\n");
    while(!is_empty(&r)){
        element = dequeue(&r);
        printf("꺼내진 정수: %d \n", element);
        print_queue(&r);
    }

    printf("큐는 공백상태 입니다.");

    return 0;
    


}