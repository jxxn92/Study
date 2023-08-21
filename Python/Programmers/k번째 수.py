array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	
answer = []
lst = []

for i in range(len(commands)):
    first = commands[i][0]
    last = commands[i][1]
    n = commands[i][2]
    lst.append(sorted(array[first-1:last]))
    answer.append(lst[0][n-1])
    lst.clear()
    print(answer)
    