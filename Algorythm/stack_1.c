#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100

typedef int element;
element stack[MAX_SIZE];
int top  = -1;

// empty, full, push, pop, peak, main

int is_empty(){
    if(top == -1){
        return 1;
    }
    return 0;
}

int is_full(){
    if(top == MAX_SIZE-1){
        return 1;
    }
    return 0;
}

void push(element data){
    if(is_full()){
        fprintf(stderr,"Stack is FULL\n");
    }
    stack[++top] = data; // 지금 현재 스택이 비어있다고 가정하면 top 이 -1을 가리키기 때문에 먼저 상향을 한 후에 값을 넣어줘야한다.
}

element pop(){
    if(is_empty()){
        fprintf(stderr,"Stack is Eempty\n");
    }
    return stack[top--];
}

element peek(){
    if(is_empty()){
        fprintf(stderr, "Stack is Empty\n");
    }
    return stack[top];
}

int main(void){

    push(3);
    push(4);
    push(5);

    pop();

    printf("%d\n",peek());

}