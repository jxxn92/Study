#include <stdio.h>
#include <stdlib.h>
#define MAX_STACK_SIZE 100
#define MAX_STRING 100

typedef struct{
    int student_no;
    char name[MAX_STRING];
    char address[MAX_STRING];
} element;

element stack[MAX_STACK_SIZE];
int top = -1;

int is_empty(){
    if(top == -1){
        return 1;
    }
    return 0;
}

int is_full(){
    if(top == (MAX_STACK_SIZE-1)){
        return 1;
    }
    return 0;
}

void push(element data){
    if(is_full()){
        fprintf(stderr, "Stack is Full");
        return;
    }
    stack[++top] = data;
}

element pop(){
    if(is_empty()){
        fprintf(stderr, "Stack is Empty");
        exit(1);
    }
    return stack[top--];
}

element peek(){
    if(is_empty()){
        fprintf(stderr, "Stack is Empty");
        exit(1);
    }
    return stack[top];
}

int main(void){
    element ie = { 20230001, "Hong", "Seoul" };
    element oe;

    push(ie);
    oe = pop();

    printf("학번 : %d \n",oe.student_no);
    printf("이름 : %s \n",oe.name);
    printf("주소 : %s \n",oe.address);
}
