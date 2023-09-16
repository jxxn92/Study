import sys
from collections import deque
input = sys.stdin.readline 

answer = []
num, idx = map(int, input().split())

queue = deque([i for i in range(1, num+1)])

while queue:
    for _ in range(idx-1):
        queue.append(queue.popleft())

    answer.append(queue.popleft())

result = ", ".join(map(str, answer))
print("<",result,">", sep='')

# 이거랑 비슷하게 아이디어 내긴 했는데 최적화 진자 잘한 블록그 있어서 가져온거긴한데 아이디어는 같은데 최적화가 진짜 실력을 가르는 것 같다.