import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

arr = [0] * 91

arr[1] = 1
arr[2] = 1
for i in range(3, 91):
    arr[i] = arr[i-2] + arr[i-1]

n = int(input())
print(arr[n])