array = [7,77,17]
answer = []
count = 0
# lst = [array[i:i+1] for i in range(0,len(array))]
for i in range(len(array)):
    lst = str(array[i:i+1])  
    for j in lst:
        answer.append(j)
x = ''
for x in answer:
    if x == '7':
        count += 1

print(count)