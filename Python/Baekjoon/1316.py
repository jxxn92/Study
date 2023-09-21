import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    s = str(input().rstrip())
    lst = list(s)
    print(lst)