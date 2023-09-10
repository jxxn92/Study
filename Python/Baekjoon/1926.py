import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]

picture = 0
pictures = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x,y):
    global picture

    graph[x][y] = 0
    picture += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        
        if graph[nx][ny] == 1:
            dfs(nx, ny)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            picture = 0
            dfs(i, j)
            pictures.append(picture)
pictures.sort()

if len(pictures) == 0:
    print(0)
    print(0)
else:
    print(len(pictures))
    print(pictures[-1])