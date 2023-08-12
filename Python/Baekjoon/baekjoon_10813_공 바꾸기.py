n,m = input().split()

lst = list(range(1,int(n)+1))

for i in range(int(m)):
    tmp = 0 
    a, b = input().split()
    tmp = lst[int(a)-1]
    lst[int(a)-1] = lst[int(b)-1]
    lst[int(b)-1] = tmp
string = ' '.join(map(str, lst))
print(string)


