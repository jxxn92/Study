numbers = [5,0,2,7]
numbers.sort()
# [1, 1, 2, 3, 4]
lst = []
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        lst.append((numbers[i]+numbers[j]))
lst = list(set(lst))
lst.sort()
print(lst)