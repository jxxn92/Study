from collections import deque
n, cnt = map(int, input().split())
idx = 0
lst = []
q = deque(range(1,n+1))
print(q)

while (len(q) > 1):
    if idx == 0:
        left_num = q.popleft()
        q.append(left_num)
        idx += 1
    if (idx % (cnt-1) != 0):
        left_num = q.popleft()
        q.append(left_num)
        idx += 1
    else:
        left_num = q.popleft()
        lst.append(left_num)
        idx = 0
lst.append(q.pop())
# N = len(lst)
# print('<', end="")
# for i in range(N):
#     if (i != N -1):
#         print(f'{lst[i]}, ', end="")
#     else:
#         print(f'{lst[i]}', end="")
# print('>', end="")

import math
import time

start = time.time()
math.factorial(100000)
end = time.time()

print(f"{end - start:.5f} sec")