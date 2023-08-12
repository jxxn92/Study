import math
a = 1
b = 16

b //= math.gcd(a,b)

while b % 2 == 0:
    b //= 2
while b % 5 == 0:
    b //= 5

print(1) if b == 1 else 2
