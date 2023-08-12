#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100

typedef int element;

typedef struct StackType
{
    element stack[MAX_SIZE];
    int top;
} StackType;

void init(StackType *s){
    s -> top = -1;
}

int is_empty(StackType *s){
    if(s -> top == -1 ){
        return 1;
    }
    return 0;
}

int is_full(StackType *s){
    if(s->top == MAX_SIZE-1){
        return 1;
    }
    return 0;
}

void push(StackType *s, element data){
    if(is_full(s)){
        fprintf(stderr,"Stack is FULL");
    }

    s->stack[++(s->top)]= data; 
}

element pop(StackType *s){
    if(is_empty(s)){
        fprintf(stderr, "Stack is Empty");
    }
    return s->stack[(s->top)--];
}

element peek(StackType *s){
    if(is_empty(s)){
        fprintf(stderr, "Stack is Empty");
    }
    return s->stack[s->top];
}

int main(void){
    StackType s;
    init(&s);

    push(&s, 3);
    push(&s, 4);
    push(&s, 5);

    pop(&s);
    printf("%d\n",peek(&s));
}