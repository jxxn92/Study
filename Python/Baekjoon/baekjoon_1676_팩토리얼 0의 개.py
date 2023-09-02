import sys
lst = []
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
n = int(sys.stdin.readline())
k = str(factorial(n)).count('0')
print(k)