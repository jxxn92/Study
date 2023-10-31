import sys
input = sys.stdin.readline

n = int(input())
change = 1000-n

number = 0

while(change >= 0):
    if change >= 500:
        number += (change // 500)
        change = (change % 500)
    elif change >= 100:
        number += (change // 100)
        change = (change % 100)
    elif change >= 50:
        number += (change // 50)
        change = (change % 50)
    elif change >= 10:
        number += (change // 10)
        change = (change % 10)
    elif change >= 5:
        number += (change // 5)
        change = (change % 5)
    else:
        number += (change)
        break
print(number)