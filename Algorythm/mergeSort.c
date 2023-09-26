#include <stdio.h>
#define MAX_SIZE 8
void merge_sort(int list[], int left , int right);
void merge(int list[], int left, int mid, int right);

int sorted[MAX_SIZE];

void merge_sort(int list[], int left , int right) {
    int mid;
    if (left < right) {
        mid = (left+right) / 2;
        merge_sort(list, left , mid);
        merge_sort(list, mid+1, right);
        merge(list, left, mid, right);
    }
}

void merge(int list[], int left, int mid, int right) {
    int i, j, k, l;
    i, k = left;
    j = mid+1;

    while(i <= mid && j <= right) {
        if(list[i] <= list[j]) {
            sorted[k++] = list[i++];
        } else {
            sorted[k++] = list[j++];
        }
    }
    if( i > mid) {
        for(l=j; l <= right; l++){
            sorted[k++] = list[l];
        } 
    } else {
        for(l = i; i <= mid; i++){
            sorted[k++] = list[l];
        }
    }

    for(l=left; l<=right; l++){
        list[l] = sorted[l];
    }
}

void main(){
    int i;
    int n = MAX_SIZE;
    int list[MAX_SIZE] = {21, 10, 12, 20, 25, 13, 15, 22};

    // 합병 정렬 수행(left: 배열의 시작 = 0, right: 배열의 끝 = 7)
    merge_sort(list, 0, n-1);

    // 정렬 결과 출력
    for(i=0; i<n; i++){
        printf("%d\n", list[i]);
    }
}