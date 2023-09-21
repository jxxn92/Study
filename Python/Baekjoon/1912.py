import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

print(arr)
print(arr[-1]+arr[-2])
