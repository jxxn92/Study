t = "500220839878"
p = "7"
l = len(p)
lst = []
lst2 = []
answer= []

for i in range(len(t)):
    lst.append(t[i:i+l])
print(lst)

for i in lst:
    if len(i) == l:
        lst2.append(i)

print(lst2)

for i in lst2:
    if int(i) <= int(p):
        answer.append(i)
print(len(answer))