import sys
import math
from itertools import combinations
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

s = 0


for _ in range(int(input())):
    arr = list(map(int, input().split()))
    del arr[0]

    lst = list(combinations(arr,2))

    for i in range(len(lst)):
        s += math.gcd(lst[i][0],lst[i][1])
        arr.clear() 
    print(s)
    s = 0