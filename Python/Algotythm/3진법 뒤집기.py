n = 45
tbin = []
while n != 0:
    tbin.append(n % 3)
    n //= 3
print(tbin)
# if tbin[-1] != 0:
#     s = 1
# else:
#     s = 0
s = 0
i = 0
while len(tbin) != 0:
    a = tbin.pop()
    s = s + (a*(3**i))
    i+=1
print(s)

