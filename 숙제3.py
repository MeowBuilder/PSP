from asyncio import graph
from collections import deque

# 실습 음료수 얼려 먹기
'''
4 5
00110
00011
11111
00000
'''
"""
def bfs(r,c):
    queue = deque([(r,c)])
    graph[r][c] = 1
    while queue:
        r,c = queue.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and graph[nr][nc] == 0:
                graph[nr][nc] = 1
                queue.append((nr,nc))

def dfs_stack(r,c):
    stack = deque([(r,c)])
    while stack:
        r,c = stack.pop()
        if graph[r][c] == 0:
            graph[r][c] = 1
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and graph[nr][nc] == 0:
                    stack.append((nr, nc))

def dfs(r,c):
    graph[r][c] = 1
    for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr,nc = r+dr,c+dc
        if 0 <= nr < R and 0 <= nc < C and graph[nr][nc] == 0:
            dfs(nr,nc)
    pass
R,C = map(int, input().split())
graph = [list(map(int,input())) for _ in range(R)]
ICE = 0
for r in range(R):
    for c in range(C):
        if graph[r][c] == 0:
            ICE += 1
            bfs(r,c)

print(ICE)
"""
# 실습 미로 탈출
"""
'''
5 6
101010
111111
000001
111111
111111
'''
def bfs(r,c):
    queue = deque([(r,c)])
    while queue:
        r,c = queue.popleft()
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr,c+dc
            if 0 <= nr < R and 0 <= nc < C and graph[nr][nc] == 1:
                graph[nr][nc] = graph[r][c] + 1
                queue.append((nr, nc))
R,C = map(int, input().split())
graph = [list(map(int,input())) for _ in range(R)]
bfs(0,0)
print(graph)
print(graph[R-1][C-1])

#[[3, 0, 5, 0, 7, 0],
# [2, 3, 4, 5, 6, 7],
# [0, 0, 0, 0, 0, 8],
# [14, 13, 12, 11, 10, 9],
# [15, 14, 13, 12, 11, 10]]
"""

# 숙제 1. 백준 DFS와 BFS
"""
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

N,M,V = map(int, input().split())
graph = [[False] * (N+1) for _ in range(N+1)]
for i in range(M):
    S,E = map(int, input().split())
    graph[S][E] = True
    graph[E][S] = True

visited = [False] * (N+1)
dfs(V)
print('')

visited = [False] * (N+1)
bfs(V)
"""

# 숙제 2. 백준 숨바꼭질
"""
from collections import deque

def bfs(N):
    distance = 0
    Visited.add(N)
    queue = deque([(N,distance)])
    while queue:
        X,distance = queue.popleft()
        if X == K:
            print(distance)
            break
        for NX in [X-1,X+1,2*X]:
            if 0<=NX<=100000 and NX not in Visited:
                Visited.add(NX)
                queue.append((NX,distance+1))



N,K = map(int, input().split())
Visited = set()
bfs(N)
"""
"""
#교수님 답
def BFS(N):
    distance = 0
    Visited[N] = True
    queue = deque([(N,distance)])
    while queue:
        X,dis = queue.popleft()
        if X == K:
            print(dis)
            break
        for NX in [X-1,X+1,2*X]:
            if 0<=NX<=100000 and not Visited[NX]:
                Visited[NX] = True
                queue.append((NX,dis+1))


N,K = map(int, input().split())
Visited = [False] * 100001
BFS(N)
"""

# 숙제 3. TUKorea 중요한 교차로
"""
def DFS(v, i, graph, N, visited):
    visited[v] = True
    for c in range(N):
        if c != i and graph[v][c] and not visited[c]:
            DFS(c, i, graph, N, visited)

N,M = map(int, input().split())
graph = [[False] * (N) for _ in range(N)]

for _ in range(M):
    S,E = map(int, input().split())
    graph[S-1][E-1] = True
    graph[E-1][S-1] = True

answer = []
for i in range(N):
    visited = [False] * N
    v = (i+1) % N
    DFS(v,i,graph,N,visited)
    
    for c in range(N):
        if i != c and not visited[c]:
            answer.append(i+1)
            break
print(len(answer))
for a in answer:
    print(a)
"""
"""
from collections import deque
def DFS(v,i):
    stack = deque([V])
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            for adj in graph[node]:
                if adj != i and not visited[adj]:
                    stack.append(adj)


N,M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    S,E = map(int, input().split())
    graph[S].append(E)
    graph[E].append(S)

answer = []

for i in range(1,N+1):
    visited = [False] * (N+1)
    if i == 1: V = 2
    else: V = 1
    DFS(V,i)
    for j in range(1,N+1):
        if j != i and not visited[j]:
            answer.append(i)
            break
print(len(answer))
for a in answer:
    print(a)
"""

# 숙제 4. 프로그래머스 여행경로
"""
def DFS(port,path,graph,ports,nTickets):
    r = ports.index(port)
    for c in range(len(ports)):
        if graph[r][c] > 0:
            graph[r][c] -= 1
            port = ports[c]
            nTickets -= 1
            (answer,nTickets) = DFS(port,path+[port],graph,ports,nTickets)
            if nTickets == 0:
                return (answer,nTickets)
            else:
                graph[r][c] += 1
                nTickets += 1
            
    return (path,nTickets)


def solution(tickets):
    ports = set()
    for path in tickets:
        ports = ports.union(set(path))
    ports = sorted(list(ports))
    
    N = len(ports)
    graph = [[0] * N for _ in range(N)]
    for [a,b] in tickets:
        r = ports.index(a)
        c = ports.index(b)
        graph[r][c] += 1

    nTickets = len(tickets)
    port = 'ICN'
    path = ['ICN']
    (answer,nTickets) = DFS(port,path,graph,ports,nTickets)
    
    return answer
"""
"""
# DFS 재귀, preorder traversal, node -> left -> right
def DFS(port,path,graph,ports,nTickets):
    r = ports.index(port)
    for c in range(len(ports)):
        if graph[r][c] > 0:
            graph[r][c] -= 1
            nTickets -= 1
            port = ports[c]
            (answer,nTickets) = DFS(port,path+[port],graph,ports,nTickets)
            if nTickets == 0:
                return (answer,nTickets)
            else:
                graph[r][c] += 1
                nTickets += 1
    return (path,nTickets)

def solution(tickets):
    ports = set()
    for [a,b] in tickets:
        ports.add(a)
        ports.add(b)
    ports = list(ports)
    ports.sort()

    N = len(ports)
    graph = [[0] * N for _ in range(N)]
    for [a,b] in tickets:
        r = ports.index(a)
        c = ports.index(b)
        graph[r][c] += 1
    nTickets = len(tickets)
    port = 'ICN'
    path = ['ICN']
    (answer,nTickets) = DFS(port,path,graph,ports,nTickets)
    return answer
"""
# 숙제 5. 백준 알파벳 // 시간초과
def DFS(r, c, path, MAX_PATH):
    if len(path) > len(MAX_PATH):
        MAX_PATH = path[:]
        if len(MAX_PATH) > 26:
            return MAX_PATH
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C and graph[nr][nc] not in path:
            MAX_PATH = DFS(nr,nc,path+[graph[nr][nc]],MAX_PATH)
    return MAX_PATH

R,C = map(int, input().split())
graph = [list(input()) for _ in range(R)] #한글자한글자 입력받으려면 그냥 input
r,c = 0,0
path = [graph[r][c]]
MAX_PATH = []
MAX_PATH = DFS(r,c,path,MAX_PATH)
print(len(MAX_PATH))


# 숙제 6. 백준 섬의 개수
"""
from collections import deque
def bfs(r,c):
    queue = deque([(r,c)])
    graph[r][c] = 0
    while queue:
        r,c = queue.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and graph[nr][nc] == 1:
                graph[nr][nc] = 0
                queue.append((nr, nc))

while True:
    C,R = map(int, input().split())
    if R == 0 and C == 0:
        break
    graph = [list(map(int,input().split())) for _ in range(R)]
    count = 0
    for r in range(R):
        for c in range(C):
            if graph[r][c] == 1:
                count += 1
                bfs(r,c)
    print(count)
"""

# 자습. 백준 안전 영역
"""
import sys
sys.setrecursionlimit(10**6)
def DFS(r,c):
    visited[r][c] = True
    for nr,nc in [[r-1,c],[r+1,c],[r,c-1],[r,c+1]]:
        if 0 <= nr < N and 0 <= nc < N and graph[nr][nc] > i and not visited[nr][nc]:
            DFS(nr,nc)


N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
max_height = 0
res = []

for r in graph:
    for c in r:
        max_height = max(max_height,c)

for i in range(max_height+1):
    count = 0
    visited = [[False] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if graph[r][c] > i and not visited[r][c]:
                count += 1
                DFS(r,c)
    res.append(count)

print(max(res))
"""