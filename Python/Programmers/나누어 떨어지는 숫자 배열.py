arr = [3,2,6]
divisor = 10
answer = []

for i in arr:
    if i % divisor == 0:
        answer.append(i)
answer.sort()
if len(answer) == 0:
    print([-1])
else:
    print(answer)
