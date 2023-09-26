import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(1, n+1):
    s = str(input().rstrip())
    if s != 'ENTER':
        arr.append(s)
se = set(arr)
print(len(se))
