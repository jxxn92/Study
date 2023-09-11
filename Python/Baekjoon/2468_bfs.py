import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
graph = []
answer = []
max_num = 0

for i in range(n):
    graph.append(list(map(int, input().rstrip().split())))
    
    for j in range(n):
        if max_num < graph[i][j]:
            max_num = graph[i][j]

def bfs(x, y, num):
    
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > num and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

for i in range(max_num):
    cnt = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]

    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0:
                bfs(j,k,i)
                cnt += 1
        answer.append(cnt)
answer.sort()
print(answer[-1])
