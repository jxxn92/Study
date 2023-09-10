import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

graph = []
result = []
answer = []
# 상, 하, 좌, 우, 좌상, 좌하, 우상, 우하
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

def dfs(x,y):

    graph[x][y] = 0
    
    for i in range(8):
        nx = x + dx[i] 
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        
        if graph[nx][ny] == 1:
            dfs(nx, ny)




while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    else:
        for i in range(n):
            graph.append(list(map(int, input().rstrip().split())))
        for k in range(n):
            for j in range(m):
                if graph[k][j] == 1:
                    dfs(k,j)
                    result.append(1)
        answer.append(len(result))
        graph = []
        result = []

for i in range(len(answer)):
    print(answer[i])