#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_SIZE 100

typedef int element;

typedef struct {
    element data[MAX_SIZE];
    int top;
} StackType;

void init_stack(StackType *s){
    s->top = -1;
}

int is_empty(StackType *s){
    return (s->top == -1);
}

int is_full(StackType *s){
    return (s->top == MAX_SIZE -1);
}

void push(StackType *s, element item){
    if(is_full(s)){
        fprintf(stderr, "Stack Overflow");
        exit(1);
    }
    s->data[++(s->top)] = item;
}

element pop(StackType *s){
    if(is_empty(s)){
        fprintf(stderr, "Stack is Empty");
        exit(1);
    }
    return s->data[(s->top)--];
}

element peek(StackType *s){
    if(is_empty(s)){
        fprintf(stderr, "Stack is Empty");
        exit(1);
    }
    return s->data[s->top];
}

int main(void){

    StackType s;
    init_stack(&s);

    int count = 0;
    printf("정수 배열의 크기: ");
    scanf("%d", &count);

    return 0;
}