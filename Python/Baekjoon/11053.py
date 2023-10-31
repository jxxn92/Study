import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

lst = []
lst.append(arr[0])
for i in range(1, n):
    if arr[i] == 0:
        arr[i] = arr[i-1]
    if arr[i] > arr[i-1]:
        lst.append(arr[i])
print(lst)
print(len(lst))