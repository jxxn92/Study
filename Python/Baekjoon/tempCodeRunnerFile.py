import sys
basket,n = map(int, sys.stdin.readline().split())

lst = [i for i in range(1,basket+1)]
lst2 = []
lst3 = []
lst4 = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if b-a == 1:
        tmp = lst[a-1]
        lst[a-1] = lst[b-1]
        lst[b-1] = tmp
    else:
        for i in range(a-1,b):
            lst2.append(lst[i])
        for i in range(a-1,b):
            lst[i] = lst2.pop()
print(lst)


