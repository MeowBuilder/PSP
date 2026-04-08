# 백준 안전 영역
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
# 백준 ATM
"""
N = int(input())
p = list(map(int,input().split()))
wait_time = 0
time = 0
while p:
    cur_time = min(p)
    time += wait_time+cur_time
    wait_time += cur_time
    p.remove(cur_time)
print(time)
"""