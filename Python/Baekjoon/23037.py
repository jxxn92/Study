import sys
input = sys.stdin.readline

n = str(input().rstrip())
s = 0
for i in range(len(n)):
    s += (int(n[i]))**5
print(s)