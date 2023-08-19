absolutes = [4,7,12]
signs = [True,False,True]
answer = []
lst = []
for i in range(len(absolutes)):
    s = str(signs[i]) + str(absolutes[i])
    answer.append(s)

for i in range(len(answer)):
    if 'True' in answer[i]:
        answer[i] = answer[i].replace('True','+')
    elif 'False' in answer[i]:
        answer[i] = answer[i].replace('False','-')
for i in range(len(answer)):
    lst.append(int(answer[i]))

print(sum(lst))