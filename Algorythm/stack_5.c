#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100

typedef int element;

typedef struct{
    element stack[MAX_SIZE];
    int top;
} StackType;

void init_stack(StackType *s){
    s->top = -1;
}

int is_empty(StackType *s){
    if(s->top == -1){
        return 1;
    }
    return 0;
}
int is_full(StackType *s){
    if(s->top == (MAX_SIZE-1)){
        return 1;
    }
    return 0;
}

void push(StackType *s, element data){
    if(is_full(s)){
        fprintf(stderr, "Stack is Full");
        exit(1);
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
    StackType *s;
    s = (StackType *)malloc(sizeof(StackType)); // 동적할당

    init_stack(s);

    push(s, 1);
    push(s, 2);
    push(s, 3);

    printf("%d \n", pop(s));
    printf("%d \n", pop(s));
    printf("%d \n", pop(s));

    free(s);
}