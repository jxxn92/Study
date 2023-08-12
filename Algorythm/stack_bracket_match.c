#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_SIZE 100

typedef int element;

typedef struct StackType
{
    element stack[MAX_SIZE];
    int top;
} StackType;

int init_stack(StackType *s){
    s->top = -1;
}

int is_empty(StackType *s){
    if(s->top == -1){
        return 1;
    }
    return 0;
}

int is_full(StackType *s){
    if(s->top == (MAX_SIZE -1)){
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

int check_matching(const char *in){

    StackType s;

    char ch, pop_ch; 
    /*
    * ch 는 in 포인터에서 한글자씩 떼서 저장할 변수
    * pop_ch 는 스택에 들어갔다가 pop 했을 때 저장될 변수
    * stack [ {, [, ( ]   
    * ch = ')' pop_ch = ')' => 조건을 만족 하므로 정상적으로 pop 이후 뒤 코드로 이동
    */

    int i, n = strlen(in);
    init_stack(&s);

    for(i = 0; i < n; i++){
        ch = in[i];

        switch (ch){
            case '(' :
            case '{' :
            case '[' :
                push(&s, ch);
                break;
            case ')' :
            case '}' :
            case ']' :
                if(is_empty(&s)) return 0;
                else{
                    pop_ch = pop(&s);
                    if(( pop_ch == '(' && ch != ')' ) ||
                    (   pop_ch == '{' && ch != '}' ) ||
                    (   pop_ch == '[' && ch != ']' )){
                        return 0;
                    } 
                    break;
                }
        }
    }
    if(!is_empty(&s)){
        return 0;
    }
    return 1;
}

int main(void){
    char *p = "{ A[(i+1)]=0 }";
    if( check_matching(p) == 1){
        printf("%s 괄호 검사 성공 ! \n", p);
    }
    else{
        printf("%s 괄호 검사 실패", p);
    }
    return 0;
}