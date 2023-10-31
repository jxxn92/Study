import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

width = int(input())

arr = [0] * 1001
arr[0] = 1
arr[1] = 1

for i in range(2, 1001):
    arr[i] = arr[i-1] + arr[i-2]


print(arr[width] % 10007)