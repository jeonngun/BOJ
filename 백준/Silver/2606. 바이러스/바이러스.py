Node = int(input())
Edge = int(input())
graph = [[] for j in range(Node+1)]
for i in range(Edge):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)
visited = [False]*(Node+1)

count = 0
def dfs(x):
    global count
    visited[x] = True
    for k in sorted(graph[x]):
        if not visited[k]:
            dfs(k)
            count += 1
    return count

print(dfs(1))