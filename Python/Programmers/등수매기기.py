score = [[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]
lst = []
answer = []

for i in score:
    lst.append(sum(i)/len(i))
sort_lst = sorted(lst, reverse=True) 

for i in lst:
    answer.append(sort_lst.index(i)+1)