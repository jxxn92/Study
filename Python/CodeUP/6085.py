a, b, c = map(int,input().split())
g = (a*b*c)
f=g/8
h=f/1024/1024
e = round(h, 2)
x = "MB"
print(f"{e:.2f} {x}")
