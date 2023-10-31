import sys
from itertools import permutations
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

arr = list(map(str, input().rstrip()))
n = len(arr)

p = list(permutations(arr, n))
lst = []
for i in p:
    s = ''.join(i)
    
    if(int(s)  % 30 == 0):
        lst.append(int(s))
if len(lst) == 0:
    print(-1)
else:
    print(lst[-1])