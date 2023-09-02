# baekjoon 1457 방 번호
import math
lst = [0] * 10

num = input()
for i in num:
    if int(i) == 6:
        lst[-1] += 1
    else:
        lst[int(i)] += 1

if lst.index(max(lst)) == 9:
    print(math.ceil(max(lst)/2))
else:
    print(max(lst))