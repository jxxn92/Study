import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

vertex, edge = map(int, input().split())
graph = [[] for _ in range(vertex + 1)]
visited = [False] * (vertex + 1)

for _ in range(edge):
    v1, v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(graph, num, visited):
    
    visited[num] = True

    for i in graph[num]:
        if not visited[i]:
            dfs(graph, i, visited)

cnt = 0

for i in range(1, vertex+1):
    if not visited[i]:
        dfs(graph, i, visited)
        cnt += 1
print(cnt)