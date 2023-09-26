# include <stdio.h>
# define SWAP(x, y, temp) ( (temp)=(x), (x)=(y), (y)=(temp) )
# define MAX_SIZE 5

void selection_sort(int list[], int n) {
    int indexmin, temp;

    for(int i = 0; i < n-1; i++){
        indexmin = i;

        for(int j = i+1; j < n; j++) {
            if(list[j] < list[indexmin]) {
                indexmin = j;
            }
        }

        if ( i != indexmin) {
            SWAP(list[i], list[indexmin], temp);
        }
    }
}

int main(void) {
    int list[MAX_SIZE] = { 9, 6, 7, 3, 5 };

    for (int i = 0; i < MAX_SIZE; i++) {
        printf("%d ", list[i]);
    }
    printf("\n");
    // 선택 정렬 수행
    selection_sort(list, MAX_SIZE);

    // 정렬 결과 출력
    for (int i = 0; i < MAX_SIZE; i++) {
        printf("%d ", list[i]);
    }
    return 0;
}