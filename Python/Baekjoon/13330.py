# Baekjoon 13330 방 배정
#여기서 학년과 성별 사용 2차원 배열인것을 알아야하고 성별을 0,1? 이걸통해 인덱스를 사용해야 간단 하다는 것을 파악해야하낟.
import sys
import math
# student[학년 1 ~ 6][성별 0,1]
num, mx = map(int, sys.stdin.readline().split())
student = [[0]*2 for _ in range(6)]
room = 0
# [[1, 2], [2, 1], [1, 3], [0, 1], [1, 2], [1, 1]]
for i in range(num):
    sex, grade = map(int, sys.stdin.readline().split())
    student[grade-1][sex] += 1

for g in range(6):
    for s in range(2):
        if (student[g][s] > 0 and student[g][s] <= mx):
            room += 1
        else:
            room += math.ceil(student[g][s] / mx)
print(room)
