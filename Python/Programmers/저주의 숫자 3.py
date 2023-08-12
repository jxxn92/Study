answer = []
lst = []
for i in range(1,200):
    if (i % 3 != 0):
        answer.append(str(i))
for i in answer:
    if '3' not in i:
        lst.append(i)
print(lst)