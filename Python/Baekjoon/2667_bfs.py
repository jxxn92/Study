import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

house = 0 # 모여 있는 집들의 개수
result  = [] # 집들의 개수를 담을 배열

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global house
    
    queue = deque()
    queue.append((x,y))





