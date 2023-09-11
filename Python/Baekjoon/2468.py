import sys
sys.setrecursionlimit(10**8)
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

def dfs(x, y, num):

    for i in range(4):
    
        nx = x + dx[i]
        ny = y + dy[i]  

        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
            if graph[nx][ny] > num:
                visited[nx][ny] = 1
                dfs(nx, ny, num)

for i in range(max_num):
    cnt = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]

    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0:
                cnt += 1
                visited[j][k] = 1
                dfs(j, k, i)
    answer.append(cnt)
answer.sort()
print(answer[-1])