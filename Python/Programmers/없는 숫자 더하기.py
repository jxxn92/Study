numbers = [1,2,3,4,6,7,8,0]
answer = []
lst = [0,1,2,3,4,5,6,7,8,9]

for i in lst:
    if i in numbers:
        pass
    else:
        answer.append(i)

print(sum(answer))