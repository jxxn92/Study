h, b, c, s = map(int,input().split())

total = h*b*c*s
print(round(total/8/1024/1024,1),"MB")