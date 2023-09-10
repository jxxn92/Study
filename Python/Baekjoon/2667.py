import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

house = 0 # 모여 있는 집들의 개수
result  = [] # 집들의 개수를 담을 배열

# 한 점을 기준으로 상,하,좌,우 한칸씩 이동할 좌표 배열
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x,y):
    global house

    graph[x][y] = 0
    house += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        
        if graph[nx][ny] == 1:
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house = 0
            dfs(i, j)
            result.append(house)
result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])


