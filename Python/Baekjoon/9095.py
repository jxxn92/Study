import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


lst = [0] * 12

lst[1] = 1
lst[2] = 2
lst[3] = 4

for i in range(4, 12):
    lst[i] = lst[i-3] + lst[i-2] + lst[i-1]
for _ in range(int(input())):
    a = int(input())
    print(lst[a])