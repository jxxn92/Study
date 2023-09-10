import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = []

def dfs(x, y):

    graph[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if graph[nx][ny] == 1:
            dfs(nx, ny)

for _ in range(int(input())):
    m, n, k = map(int, input().rstrip().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0

    for j in range(k):
        a, b = map(int, input().split()) 
        graph[b][a] = 1

    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1:
                dfs(x,y)
                cnt += 1
    print(cnt)