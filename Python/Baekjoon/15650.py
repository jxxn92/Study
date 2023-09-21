import sys
from itertools import combinations
input = sys.stdin.readline

n,m = map(int, input().rstrip().split())
lst = [i for i in range(1, n+1)]
arr = list(combinations(lst,m))

if m == 1:
    for i in range(1,n+1):
        print(i)
else:
    for i in arr:
        print(*i)