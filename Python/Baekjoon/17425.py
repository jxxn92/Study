import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    num = int(input())
    result = 0
    for i in range(1, num + 1):
        result += (num // i) * i
    print(result)
