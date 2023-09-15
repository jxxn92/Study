import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

d = [0] * 1000001
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, 1000001):
    d[i] = (d[i-3] + d[i-2] + d[i-1]) % 1000000009

for _ in range(int(input())):
    a= int(input())
    print(d[a])
    