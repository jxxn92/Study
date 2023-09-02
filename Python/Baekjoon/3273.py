# baekjoon 3273 두 수의 합
import sys
input = sys.stdin.readline

data = []
n = int(input())
data = list(map(int, input().split()))
target = int(input())
cnt = 0

for i in range(len(data)):
    for j in range(i+1,len(data)):
        if (i+j == target):
            cnt +=1
print(cnt)