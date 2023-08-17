import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque(enumerate(map(int, input().split())))
ans = []
# deque([(0, 3), (1, 2), (2, 1), (3, -3), (4, -1)])
# [(1, 2), (2, 1), (3, -3), (4, -1)]
while q:
    idx, item = q.popleft()
    ans.append(idx+1)

    if item > 0:
        q.rotate(-(item-1))
    else:
        q.rotate(-item)

print(*ans)

#TODO Python Deque 모듈에 rotate라는 함수가 존재 
#TODO rotate 함수는 .rotate() 꼴로 사용 되는데 양수면 오른쪽으로 회전 음수면 왼쪽으로 회전 알아놓으면 유용하게 쓰일 수 있을 것 같다.