n,m = map(int,input().split())

lst = [0 for i in range(n)]

for x in range(m):
    a, b, c = map(int,input().split())
    for j in range(a-1,b):
        lst[j] = c

str1 = list(map(str, lst))
answer = ' '.join(str1)
print(answer)