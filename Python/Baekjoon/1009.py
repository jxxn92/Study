import sys

list2 = [2, 4, 8, 6]
list3 = [3, 9, 7, 1]
list4 = [4, 6]
list7 = [7, 9, 3, 1]
list8 = [8, 4, 2, 6]
list9 = [9, 1]



n = int(input())

for _ in range(n):
    a, b = map(int, input().split())

    a = (a % 10)
    if a == 0:
        print(10)
    elif a == 1:
        print(1)
    elif a == 2:
        print(list2[b%4-1])
    elif a == 3:
        print(list3[b%4-1])
    elif a == 4:
        print(list4[b%2-1])
    elif a == 5:
        print(5)
    elif a == 6:
        print(6)
    elif a == 7:
        print(list7[b%4-1])
    elif a == 8:
        print(list8[b%4-1])
    elif a == 9:
        print(list9[b%2-1])
        
    