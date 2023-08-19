import math
n = 121 
a = math.sqrt(n)
if a.is_integer():
    print(int((a+1)**2))
else:
    print(-1)

