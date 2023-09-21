#include <stdio.h>

int main(void) {
    int i , j , key;
    int arr[10] = {1, 10, 5, 8, 7, 6, 4, 3, 2, 9};

    for(int i = 1; i < sizeof(arr)/4; i++){
        key = arr[i];
        j = i-1;
        while (j >= 0 && arr[j] > key){
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = key;
    }   

    for( int k = 0; k < 10; k++){
        printf("%d, ", arr[k]);
    }

    return 0;
}