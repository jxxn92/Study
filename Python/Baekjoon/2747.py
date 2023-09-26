import sys
input = sys.stdin.readline

arr = [0] * 46
arr[1] = 1
arr[2] = 1
n = int(input())
for i in range(2,46):
    arr[i] = arr[i-2] + arr[i-1]

print(arr[n])