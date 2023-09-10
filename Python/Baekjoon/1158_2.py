import sys
from collections import deque
import math
import time
input = sys.stdin.readline
start = time.time()
math.factorial(100000)
n, k = map(int, input().split())
q = deque(range(1, n+1))
answer = []
num = k-1
idx = 0

while (len(q) > 1):
    if idx == 0:
        left_num = q.popleft()
        q.append(left_num)
        idx += 1
    if (idx % (num) != 0):
        left_num = q.popleft()
        q.append(left_num)
        idx += 1
    else:
        left_num = q.popleft()
        answer.append(left_num)
        idx = 0
answer.append(q.pop())
N = len(answer)
print('<', end="")
for i in range(N):
    if (i != N -1):
        print(f'{answer[i]}, ', end="")
    else:
        print(f'{answer[i]}', end="")
print('>', end="")

end = time.time()
print(f"{end - start:.5f} sec")