# common = [1, 2, 3, 4]
# common = [2, 4, 8]\
common = [1,2,4]
distance = []
lst = [common[i:i+2] for i in range(len(common)-1)]
# print(lst)
for i in range(0,len(common)-1):
    distance.append(common[i+1]-common[i])
tmp = distance[0]
if distance[0] == distance[1]:
    for i in range(len(distance)):
        distance.remove(tmp)
    if len(distance) == 0:
        print(common[-1] + tmp)
else:
    if distance[0] == 1:
        sequence = distance[1]
    else:
        sequence = distance[1] - distance[0]
    print(common[-1]*sequence)