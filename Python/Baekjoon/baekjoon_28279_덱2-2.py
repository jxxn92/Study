import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for _ in range(n):
    s = sys.stdin.readline().split()

    if s[0] == '1':
        queue.append(s[1])
    elif s[0] == '2':
        queue.appendleft(s[1])
    elif s[0] == '3':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
    elif s[0] == '4':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif s[0] == '5':
        print(len(queue))
    elif s[0] == '6':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif s[0] == '7':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    elif s[0] == '8':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])