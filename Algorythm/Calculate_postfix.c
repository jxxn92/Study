/*
TODO 후위 연산 계산
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 100
typedef int element;

typedef struct{
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

// int prec(char op){
    // switch (op)
    // {
        // case '(' : 
        // case ')' :
            // return 0;
        // case '+' :
        // case '-' :
            // return 1;
        // case '*' :
        // case '/' :
            // return 2;
    // }
    // return -1;
// }

int eval(char *exp){
    int op1, op2, value = 0; // op1, op2 피연산자
    int len = strlen(exp);
    char ch, ch2;
    StackType s;
    init_stack(&s);

    for (int i = 0; i < len; i++){
        ch = exp[i];

        if(ch != '+' && ch != '-' && ch != '*' && ch != '/'){ // 연산자가 아니고 피연산자라면
            value = ch - '0'; // 아스키 코드로 변환해서 숫자로 스택에 삽입
            push(&s, value);
        }
        else{
            op2 = pop(&s);
            op1 = pop(&s);

            switch (ch)
            {
                case '+' :
                    push(&s, op1 + op2);
                    break;
                case '-' :
                    push(&s, op1 - op2);
                    break;
                case '*' :
                    push(&s, op1 * op2);
                    break;
                case '/' :
                    push(&s, op1 / op2);
                    break;
            }
        }
    }
    return pop(&s);
}

int main(void){

    printf("후위표기식은 82/3-32*+ \n");
    int result = eval("82/3-32*+");
    printf("결과는 %d 입니다.", result);

    return 0;
}