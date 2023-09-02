# Baekjoon 13330 방 배정
import sys
import math
lst_boy = []
lst_girl = []
lst_room = []
room_sum = 0

num, mx = map(int, sys.stdin.readline().split())

for i in range(num):
    sex, grade = map(int, sys.stdin.readline().split())

    if sex == 0:
        lst_girl.append(grade)
    else:
        lst_boy.append(grade)

for i in range(1, 7):
    lst_room.append(lst_boy.count(i))
    lst_room.append(lst_girl.count(i))

for i in range(len(lst_room)):
    if (lst_room[i] > 0 and lst_room[i] <= mx):
        room_sum += 1
    elif (lst_room[i] > mx):
        room_sum += math.ceil(lst_room[i] / mx)
print(room_sum)