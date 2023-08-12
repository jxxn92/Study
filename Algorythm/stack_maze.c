#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 100
#define MAZE_SIZE 6
typedef struct{
    short c;
    short r;
} element;

typedef struct{
    element stack[MAX_SIZE];
    int top;
} StackType;


element here = {0, 1}, entry = {0, 1};

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

char maze[MAZE_SIZE][MAZE_SIZE] = {
    {'1', '1', '1', '1', '1' , '1'},
    {'e', '0', '1', '0', '0' , '1'},
    {'1', '0', '0', '0', '1' , '1'},
    {'1', '0', '1', '0', '1' , '1'},
    {'1', '0', '1', '0', '0' , 'x'},
    {'1', '1', '1', '1', '1' , '1'}
};

void push_loc(StackType *s, short r, short c){
    if ( r < 0 || c < 0) return;
    if(maze[r][c] != '1' && maze [r][c] != '.'){

        element tmp;
        
        tmp.r = r;
        tmp.c = c;

        push(s, tmp);
    }
}

void maze_print(char maze[MAZE_SIZE][MAZE_SIZE]){
    printf("\n");
    for(int r = 0; r < MAZE_SIZE; r++){
        for (int c = 0; c < MAZE_SIZE; c++){
            printf("%c" , maze[r][c]);
        }
        printf("\n");
    }
}

int main(void){

    int r ,c;
    StackType s;

    init_stack(&s);
    here = entry;

    while(maze[here.r][here.c] != 'x'){
        r = here.r;
        c = here.c;
        maze[r][c] = '.';

        maze_print(maze);

        push_loc(&s, r - 1, c);
        push_loc(&s, r + 1, c);
        push_loc(&s, r, c - 1);
        push_loc(&s, r, c + 1);

        if (is_empty(&s)){
            printf("실패!\n");
            return;
        }
        else{
            here = pop(&s);
        }
    }

    printf("성공! \n");
    return 0;
}