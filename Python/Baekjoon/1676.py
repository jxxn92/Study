import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

s = 1
n = int(input())
for i in range(1, n+1):
    s *= i
s = str(s)[::-1]
for i in s:
    if i != '0':
        print(s.index(i))
        break