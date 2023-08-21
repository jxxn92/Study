strings =  ["bc","bcb"]
n = 1
lst = []
answer = []
for i in strings:
    tmp = i[:n]
    i = i[n:]
    # i = i.replace(tmp,"")
    i+=tmp
    lst.append(i)
lst.sort()
for i in lst:
    tmp = i[-n:]
    i = i[:-n]
    i = tmp + i
    answer.append(i)
print(answer)

# 문제 다시 보고 다시 생각해서 풀어야함 ... .아직 못품