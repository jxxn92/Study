s1 = ["a", "b", "c"]	
s2 = ["com", "b", "d", "p", "c"]	
answer = []
for x in s1:
    for i in s2:
        if x == i:
            answer.append(x)
print(answer)