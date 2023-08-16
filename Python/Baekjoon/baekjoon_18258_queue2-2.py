import sys
from collections import deque
queue_list = deque()
n = int(sys.stdin.readline())

for _ in range(n):
    a = sys.stdin.readline().split()
    if a[0] == 'push':
        queue_list.append(a[1])
    elif a[0] == 'pop':
        if len(queue_list) == 0:
            print(-1)
        else:
            print(queue_list.popleft())   
    elif a[0] == 'front':
        if len(queue_list) == 0:
            print(-1)
        else:
            print(queue_list[0])
    elif a[0] == 'back':
        if len(queue_list) == 0:
            print(-1)
        else:
            print(queue_list[-1])
    elif a[0] == 'size':
        print(len(queue_list))
    elif a[0] == 'empty':
            if len(queue_list) == 0:
                print(1)
            else:
                print(0)