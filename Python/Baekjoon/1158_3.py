from collections import deque
n, k = map(int,input().split())
q = deque(range(1,n+1))
answer = []
idx = 0

for t