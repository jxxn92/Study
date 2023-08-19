import math
n = 6; m = 4
answer = []

def lcm(a,b):
    return a*b / math.gcd(a,b)


answer.append(math.gcd(n,m))
answer.append((int(lcm(n,m))))

print(answer)