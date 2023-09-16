import sys
input = sys.stdin.readline

s = 0

n = int(input())
num = n
if n % 2 == 1:
    num += 1

for i in range(1, num):
    s += i
print(s)