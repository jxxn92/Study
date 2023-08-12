#include <stdio.h>
#include <stdlib.h>
#define MAX_SIZE 100

typedef int element;
typedef struct{
    element *stack;
    int capacity;
    int top;
} StackType;

void init_stack(StackType *s){
    s->top = -1;
    s -> capacity = 1;
    s->stack = (element *)malloc(s->capacity * sizeof(element));
}

void delete(StackType *s){
    free(s);
}

int is_empty(StackType *s){
    if(s->top == -1 ){
        return 1;
    }
    return 0;
}

int is_full(StackType *s){
    if (s->top == (MAX_SIZE -1))
    {
        return 1;
    }
    return 0;
    }

void push(StackType *s, element data)
{
    if(is_full(s)){
        s->capacity *= 2;
        s->stack = (element *)realloc(s->stack, s->capacity * sizeof(element)); 
        /*
        * realloc -> 스택의 동적할당의 크기를 변환
        * 사용법 : (타입 *)realloc(stack 이름, capacity, sizeof(타입))
        */
        
    }
    s->stack[++(s->top)] = data;
}

element pop(StackType *s){
    if(is_empty(s)){
        fprintf(stderr, "Stack is Empty");
        exit(1);
    }
    return s->stack[(s->top)--];
}

element peek(StackType *s){
    if(is_empty(s)){
        fprintf(stderr, "Stack is Empty");
        exit(1);
    }
    return s->stack[s->top];
}

int main(void){
    StackType s;
    init_stack(&s);
    push(&s, 1);
    push(&s, 2);
    push(&s, 3);
    printf("%d \n", pop(&s));
    printf("%d \n", pop(&s));
    printf("%d \n", pop(&s));
    
    delete(&s);
    return 0;
}