# 자릿수의 합을 먼저 구한다.

x = 11
s = 0
x = str(x)
for i in range(len(str(x))):
    s += int(x[i])

if int(x) % s == 0:
    print(1)
else:
    print(0)