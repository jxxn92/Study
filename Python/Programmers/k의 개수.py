i = 10
j = 50
k = 5
lst = []
cnt = 0
for i in range(i,j+1):
    lst.append(i)
# print(lst)
lst = list(str(lst))
for x in range(len(lst)):
    if lst[x] == str(k):
        cnt+=1
print(cnt)