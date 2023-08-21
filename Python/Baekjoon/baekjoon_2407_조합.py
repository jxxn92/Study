def factorial(n):
    if n > 1:
        return (n * factorial(n-1))
    else:
        return 1
a, b = map(int, input().split())
mul = a
for i in range(1,b):
    mul = mul * (a-i)
print(mul//factorial(b))
