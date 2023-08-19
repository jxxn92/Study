n = 118372
n = list(map(int,str(n)))
n.sort(reverse=True)
answer = ""
for i in range(len(n)):
    answer += str(n[i])
print(answer)