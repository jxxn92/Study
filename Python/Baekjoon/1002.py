import sys
import math
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().rstrip().split())
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
    print(distance)