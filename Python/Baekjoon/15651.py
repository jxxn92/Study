from itertools import product

num, rep = map(int, input().split())
s = ''

for i in range(1,num+1):
    s+=str(i)

for element in product(s, repeat=rep):
    print(' '.join(element))