#include <stdio.h>
#define MAX_SIZE 5

void insert_sort(int list[], int size) {
    int key, i , j;

    // 일단 맨 앞의 하나의 원소는 정렬되어 있다고 가정
    // 삽입 정렬은 순서를 넘어가면 앞의 정수들은 모두 정렬 되어있다고 생각
    for(i = 1; i < size; i++){
        key = list[i];
        
        // 자기의 인덱스부터 0 까지의 인덱스까지 값을 줄이고 전값이 지금 현재 인덱스 값보다 클때까지 값을 줄인다음 값을 교환한다.
        // 그 전의 값들은 이미 정렬되어있다고 생각하기 때문에 조건을 만족할 때까지만 줄인다음 값을 교환한다.
        for(j = i-1; j >= 0 && list[j] > key; j--) {
            list[j+1] = list[j];        
        list[j] = key;
        }
    }
}

void main(){
    int i;
    int n = MAX_SIZE;
    int list[MAX_SIZE] = {8, 5, 6, 2, 4};

  // 삽입 정렬 수행
  insert_sort(list, n);

  // 정렬 결과 출력
  for(i=0; i<n; i++){
    printf("%d\n", list[i]);
  }
}
