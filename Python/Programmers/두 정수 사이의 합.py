a = 3
b = 5
s = 0
if a>= b:
    for i in range(b,a+1):
        s+=i
elif b>=a:
    for i in range(a,b+1):
        s+=i
print(s)