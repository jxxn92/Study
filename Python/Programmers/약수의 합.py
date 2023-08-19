n = 12
answer = []
s = 0
for i in range(1,n+1):
    if n % i == 0:
        answer.append(i)

for i in range(len(answer)):
    s += answer[i]
print(s)