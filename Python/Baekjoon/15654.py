import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

arr = list(permutations(lst, m))
for i in arr:
    print(*i)