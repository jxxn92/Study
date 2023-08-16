// 이건 그냥 ListArray
// 내일은 링크드 리스트 공부할것! 영어도 같이해라 
#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 10

typedef int element;

typedef struct {
    element array[MAX_SIZE];
    int size;
} ListArray;

void init_array(ListArray *l){
    l->size = 0;
}

void error(char *message){
    fprintf(stderr, "%s\n", message);
    exit(1);
}

int is_empty(ListArray *l){
    return l->size == 0;
}

int is_full(ListArray *l){
    return (l->size == MAX_SIZE);
}

int get_entry(ListArray *l, int pos){ // pos 위치의 값을 반환하는 함수
    if (pos < 0 || pos >= l->size){
        error("POS Error");
    }
    return l->array[pos];
}

void print_list(ListArray *l){
    for(int i = 0; i < l->size; i++)
        printf(" %d |",l->array[i]);
    printf("\n");
}

void insert_last(ListArray *l, element item){
    if(l->size >= MAX_SIZE){
        error("List Overflow");
    }
    l->array[l->size++] = item;
}

void insert_first(ListArray *l, element item){
    if(is_full(l) && (l->size) >= MAX_SIZE){
        error("Error");
    }
    for(int i = l->size; i >= 0; i--){
        l->array[i+1] = l->array[i];
    }
    l->array[0] = item;
    l->size++;
}

void insert(ListArray *l, int pos, element item){
    if(!is_full(l) && (pos >= 0) && (l->size >= pos)){
        for( int i = (l->size - 1); i >= pos; i--)
            l->array[i+1] = l->array[i];
        l->array[pos] = item;
        l->size++;
    }
}

element delete(ListArray *l, int pos){

    element val;

    if(pos < 0 && pos >= l->size)
        error("Error");
    val = l->array[pos];
    for(int i = pos; i < (l->size-1); i++)
        l->array[i] = l->array[i+1];
    l->size--;
    return val;
}

int main(void){
    
    ListArray l;
    init_array(&l);

    insert(&l, 0, 10);
    insert(&l, 0, 20); 
    insert(&l, 0, 30); 
    insert_last(&l, 40);
    print_list(&l);
    insert_first(&l, 50); print_list(&l);

    return 0;
}