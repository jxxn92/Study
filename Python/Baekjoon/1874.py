import sys
input = sys.stdin.readline

stack = []
operator = []
start = 1

n = int(input())

for _ in range(n):
    end = int(input())

    while start <= end:
        stack.append(start)
        operator.append('+')
        start += 1
    if stack[-1] == end:
        stack.pop()
        operator.append('-')
    else:
        print('NO')
        break
else:
    for i in operator:
        print(i)