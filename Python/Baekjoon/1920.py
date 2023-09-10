#baekjoon 1920 수 찾기

n1 = int(input())
arr = list(map(int, input().split()))

n2 = int(input())
arr2 = list(map(int, input().split()))

dic = {}

for i in arr2:
    dic[i] = 0
for i in arr:
    if i in dic.keys():
        dic[i] = 1

for i in dic.values():
    print(i)
