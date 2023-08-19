left = 24; right = 27
lst = []
answer = []
for i in range(left, right+1):
    for j in range(1,i+1):
        if i % j == 0:
            lst.append(j)      
    if len(lst) % 2 == 0:
        answer.append(i)
    else:
        answer.append(i*-1)
    lst.clear()
print(sum(answer))