import sys

lst = []
n = int(sys.stdin.readline())

for _ in range(n):
    weight, height = map(int,sys.stdin.readline().split())
    lst.append((height,weight))
sort = sorted(lst, key = lambda x : (-x[0], -x[1]))
print(sort)