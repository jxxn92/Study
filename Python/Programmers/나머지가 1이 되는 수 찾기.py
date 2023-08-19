n = 10
answer = []
for i in range(1, 1000001):
    if n % i == 1:
        answer.append(i)
print(answer[0])
