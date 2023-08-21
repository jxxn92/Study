d = [1,3,2,5,4]
d.sort()
budget = 9
answer = []
print(sum(d))
print(sum(d[:-1]))
print(sum(d[:-2]))
print(sum(d[:-3]))
if sum(d) <= budget:
    print(len(d))
else:
    for i in range(len(d)):
        for j in range(i+1,len(d)):
            for k in range(j+1,len(d)):
                    print(d[i],d[j],d[k])