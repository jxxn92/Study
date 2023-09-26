#include <stdio.h>
#define MAX_SIZE 5

void bubble_sort(int list[], int size) {
    int temp;

    for(int i = 0; i < size-1; i++) { // 반복 횟수
        for(int j = 0; j < size-i-1; j++){ // 앞뒤 바꿈
        // 바꿀때마다 맨뒤는 최대 고정 그러니까 -i
            if(list[j] > list[j+1]) {
                temp = list[j];
                list[j] = list[j+1];
                list[j+1] = temp;
            } 
        }
    }
}


void main(){
    
    int list[MAX_SIZE] = {7, 4, 5, 1, 3};

    for(int i=0; i<MAX_SIZE; i++){
        printf("%d ", list[i]);
    }
    printf("\n");

  // 버블 정렬 수행
    bubble_sort(list, MAX_SIZE);

  // 정렬 결과 출력
    for(int i=0; i<MAX_SIZE; i++){
        printf("%d ", list[i]);
    }
}
