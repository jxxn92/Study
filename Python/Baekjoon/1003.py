import sys
input = sys.stdin.readline

fib = [0] * 41
fibz = [0] * 41

fib[1] = 1
fib[2] = 1
fibz[0] = 1
fibz[2] = 1

for i in range(3, 41):
    fib[i] = fib[i-2] + fib[i-1]
for i in range(3, 41):
    fibz[i] = fibz[i-2] +fibz[i-1]



n = int(input())


for _ in range(n):
    num = int(input())
    print(fibz[num],fib[num])
