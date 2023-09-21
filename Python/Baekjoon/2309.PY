import sys
from itertools import combinations
input = sys.stdin.readline

lst = []
height = []
arr2 = []
idx = 0

for _ in range(9):
    lst.append(int(input()))

arr = list(combinations(lst,7))
for i in arr:
    height.append((sum(i)))

for i in height:
    if i == 100:
        idx = height.index(i)

for i in arr[idx]:
    arr2.append(i)
arr2.sort()

for i in arr2:
    print(i)