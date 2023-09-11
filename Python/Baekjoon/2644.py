vertex = int(input())
s, e = map(int, input().split())

graph = [[] for _ in range(vertex + 1)]
visited = [False] * ( vertex + 1)
answer = []

for _ in range(int(input())):
    e1, e2 = map(int, input().split())

    graph[e1].append(e2)
    graph[e2].append(e1)

def dfs(graph, s, visited, cnt):
    visited[s] = True
    cnt += 1
    
    if s == e:
        answer.append(cnt)
    
    for i in graph[s]:
        if not visited[i]:
            dfs(graph, i, visited, cnt)
dfs(graph, s, visited, 0)
if len(answer) == 0:
    print(-1)
else:
    print(answer[0] - 1)