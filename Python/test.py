# from itertools import combinations

# data = [3, 30, 34, 5, 9]

# for items in combinations(data,3):
#     num = int(str(items[0]) + str(items[1]) + str(items[2]))
#     print(num)
import sys
input = sys.stdin.readline

cards = [i for i in range(1,21)]
for _ in range(10):
    a,b = map(int,input().split())
    a-=1
    cards[a:b] = cards[a:b][::-1]
print(*cards)