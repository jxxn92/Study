import sys
input = sys.stdin.readline

arr = []
av = 0
for _ in range(4):
    o, r = map(int, input().split())
    av -= o
    av += r
    arr.append(av)
arr.sort()
print(arr[-1])