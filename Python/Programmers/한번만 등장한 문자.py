string = "abcd"	

set_string = set(string)
dict_1 = {}
answer = []
for x in set_string:
    count = 0
    for i in string:
        if x == i:
            count += 1
        dict_1[x] = count

for key, value in dict_1.items():
    if value == 1:
        answer.append(key)
answer.sort()
print(answer)