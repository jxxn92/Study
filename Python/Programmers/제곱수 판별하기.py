n = 976
answer = []
for i in range(1,1001):
    if n / i == i:
        answer.append(i)
if len(answer) == 0:
    print(1)
else:
    print(2)