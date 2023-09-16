import sys
input = sys.stdin.readline

def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)

n, m = map(int, input().split())

numerator  = factorial(n)
denominator = factorial(n-m)*factorial(m)

ans = str(int(numerator/denominator))[::-1]
cnt = 1

for i in ans:
    if i != 0:
        cnt += 1
        break
print(cnt)