N, M, V = map(int, input().split())
graph = [[]]
visited = [False]*(N+1)
for m in range(N):
    graph.append([])
for n in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)
dfs(graph, V, visited)
# 여기까지 dfs
print()

from collections import deque

visited = [False]*(N+1)
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for j in sorted(graph[v]):
            if not visited[j]:
                queue.append(j)
                visited[j] = True

bfs(graph, V, visited)