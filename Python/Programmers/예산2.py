d = [1,1,1]
budget = 2
d.sort()
answer = []
# d = [1, 2, 3, 4, 5]
cnt = 0
if sum(d) <= budget:
    print(len(d))
else:
    for i in d:
        budget -= i 
        cnt += 1
        if budget == 0:
            answer.append(cnt)
        elif budget < 0:
            answer.append(cnt-1)
print(answer[0])
