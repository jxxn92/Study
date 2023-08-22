k = 9
score =	[10, 30, 40, 3, 0, 20, 4]	
lst = []
# [10, 10, 10, 3, 0, 0, 0]
answer = []
if k > len(score):
    for _ in range(len(score)):
        lst.append(score[_])
        lst.sort()
        answer.append(lst[0])
else:
    for _ in range(k):
        lst.append(score[_])
        lst.sort()
        answer.append(lst[0])
    for i in score[k:]:
        if i >= lst[0]:
            del lst[0]
            lst.append(i)
            lst.sort()
            answer.append(lst[0])
        else:
            answer.append(lst[0])
print(answer)