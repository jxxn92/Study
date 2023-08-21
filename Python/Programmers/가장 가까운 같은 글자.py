s = "banana"
answer = []
already = []

for i in s:
    if i in already:
        answer.append(-1)
    else:
        already.append(i)
print(already)
print(answer)