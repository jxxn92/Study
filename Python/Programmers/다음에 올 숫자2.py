# common = [1, 2, 3]
common = [1, 2, 4]
distance = []
lst = [common[i:i+2] for i in range(len(common)-1)]
# print(lst)
for i in range(0,len(common)-1):
    distance.append(common[i+1]-common[i])
# print(distance)

# 등차수열인지 등비수열인지 일단 판단 해야한다.
if distance[0] == distance[1]:
    print(common[-1] + distance[0])
else:
    tmp = distance[1] // distance[0]
    print(common[-1] * tmp)