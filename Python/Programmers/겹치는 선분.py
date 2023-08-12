lines = [[0, 10], [1, 3], [4, 7]]
x1 = lines[0][0]
x2 = lines[0][1]
x3 = lines[1][0]
x4 = lines[1][1]
x5 = lines[2][0]
x6 = lines[2][1]
lst1 = []
lst2 = []
lst3 = []

for i in range(x1,x2+1):
    lst1.append(i)
for j in range(x3,x4+1):
    lst2.append(j)
for k in range(x5,x6+1):
    lst3.append(k)

print(lst1, lst2, lst3)

set1 = set(lst1) & set(lst2)
set2 = set(lst2) & set(lst3)
set3 = set(lst1) & set(lst3)
print(set1, set2, set3)

set4 = set1.union(set2)
set5 = set4.union(set3)
lst4 = list(set5)
print(lst4)

# if len(lst4) > 2:
#     print(lst4[-1]-lst4[0])
# else:
#     print(0)
# # print(set1, set2, set3)