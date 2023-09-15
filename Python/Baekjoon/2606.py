import sys
input = sys.stdin.readline

vertex = int(input())
n = int(input())
graph = [[] for _ in range(vertex + 1)]
visited = [False] * (vertex + 1)
answer = []

for _ in range(n):
    v1, v2 = map(int, input().split())
    
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(graph, idx, visited):
    visited[idx] = True

    answer.append(idx)
    for i in graph[idx]:
        if not visited[i]:
            dfs(graph, i, visited)
    return answer
# TODO 내일은 이 문제 구현해 볼것 일단 DFS 인 것 같은데 일단 구현해 보고 안되면 몰라 일단 해봐

req = dfs(graph, 1, visited)
print(len(req)-1)