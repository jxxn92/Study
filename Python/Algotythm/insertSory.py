arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

for i in range(1,len(arr)):
    key = arr[i]
    j = i - 1

    while(j >= 0 and arr[j] > key):
        arr[j+1] = arr[j]
        j -= 1
    
    arr[j+1] = key

print(arr)