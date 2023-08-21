n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
lst1 = []
lst2 = []
answer = []
for i in arr1:
    b = bin(i)[2:]
    lst1.append(b.zfill(n))
for j in arr2:
    b = bin(j)[2:]
    lst2.append(b.zfill(n))
print(lst1)
print(lst2)
for i in range(n):
    s = ''
    for j in range(n):
        if lst1[i][j] == '0' and lst2[i][j] == '0':
            s += '0'
        elif lst1[i][j] == '0' and lst2[i][j] == '1':
            s += '1'
        elif lst1[i][j] == '1' and lst2[i][j] == '0':
            s += '1'
        elif lst1[i][j] == '1' and lst2[i][j] == '1':
            s += '1'
        s = s.replace("1", "#")
        s = s.replace('0', " ")
    answer.append(s)
print(answer)