import sys
sys.setrecursionlimit(10000)


def dfs(x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    graph[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and (0 <= ny < M):
            if graph[nx][ny] == 1:
                dfs(nx, ny)

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    cnt = 0

    for _ in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1

    for x in range(N):
        for y in range(M):
            if graph[x][y] == 1:
                dfs(x, y)
                cnt += 1

    print(cnt)