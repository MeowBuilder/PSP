from collections import deque

def dfs_stack(node):
    stack = deque([node])
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            print(node, end=' ')
            for i in range(N,0,-1):
                if graph[node][i] and not visited[i]:
                    stack.append(i)

def dfs(node):
    visited[node] = True
    print(node, end=' ')
    for i in range(1,N+1):
        if graph[node][i] and not visited[i]:
            dfs(i)

def bfs(start):
    visited[start] = True
    print(start, end=' ')
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for i in range(1,N+1):
            if graph[node][i] and not visited[i]:
                queue.append(i)
                visited[i] = True
                print(i, end=' ')

# 숙제 1. 백준 DFS와 BFS

N,M,V = map(int, input().split())
graph = [[False] * (N+1) for _ in range(N+1)]
for i in range(M):
    S,E = map(int, input().split())
    graph[S][E] = True
    graph[E][S] = True

visited = [False] * (N+1)
dfs_stack(V)
print('')

visited = [False] * (N+1)
bfs(V)