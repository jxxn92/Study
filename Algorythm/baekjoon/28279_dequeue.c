// 미완성 나중에 완성해야함. 근데 사이즈 함수를 구하려면 이거 크기를 가변적으로 변경해야 할것 같은데 가능은 한데 원형함수라 아직 미숙하다... ㅅㅂ
// 1 X: 정수 X를 덱의 앞에 넣는다. (1 ≤ X ≤ 100,000) => add_rear
// 2 X: 정수 X를 덱의 뒤에 넣는다. (1 ≤ X ≤ 100,000) => add_front
// 3: 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다. => delete_rear
// 4: 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다. => delete_front
// 5: 덱에 들어있는 정수의 개수를 출력한다.  => size sizeof 함수
// 6: 덱이 비어있으면 1, 아니면 0을 출력한다. => is_empty
// 7: 덱에 정수가 있다면 맨 앞의 정수를 출력한다. 없다면 -1을 대신 출력한다. => get_rear
// 8: 덱에 정수가 있다면 맨 뒤의 정수를 출력한다. 없다면 -1을 대신 출력한다. => get_front

#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 10 

typedef int element;

typedef struct 
{
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
    return ((q->rear + 1) % MAX_SIZE == q->front );
}

void add_rear(QueueType *q, element item){
    // if 
}

void add_front(QueueType *q, element item){

}

element delete_front(QueueType *q){

}

element delete_rear(QueueType *q){

}

element get_front(QueueType *q){

}

element get_rear(QueueType *q){

}

element size(QueueType *q){
// sizeof
    return sizeof(q->data);
}

int main(void){
    QueueType q;
    
    init_queue(&q);

    printf("%d",size(&q)/sizeof(int));

    return 0;

}