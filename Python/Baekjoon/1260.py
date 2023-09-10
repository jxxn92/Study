import sys
from collections import deque
input = sys.stdin.readline

v,e,idx = map(int, input().split())

graph = [[] for i in range(v+1)] # 각 노드에 연결된 노드를 알기위해 노드를 graph 2차원 배열로 작성
visited = [False] * (v+1) # 이미 다녀온 곳들을 체크 하기 위해서 작성

for i in range(e):
    v1, v2 = map(int, input().split())
    for i in range(1, v+1):
        if v1 == i:
            graph[i].append(v2)
        if v2 == i:
            graph[i].append(v1)
        graph[i].sort()
# DFS
def dfs(graph, idx, visited):
    visited[idx] = True
    print(idx, end= ' ')

    for i in graph[idx]:
        if not visited[i]:
            dfs(graph, i, visited)
# BFS

def bfs(graph, idx, visited):
    queue = deque([idx])

    visited[idx] = True

    while queue:
        left = queue.popleft()
        print(left, end=' ')

        for i in graph[left]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(graph, idx, visited)
print()
visited = [False] * (v+1) # 값이 변경 될 걸 대비해서 dfs 출력후 bfs 출력하기전 초기화
bfs(graph, idx, visited)
    