# A 연료 채우기
import heapq

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()
L, P = map(int, input().split())
# 마을까지의 거리, 원래 연료의 양

max_heap = []
answer = 0
fuel = P
index = 0

while True:
    while index < N and arr[index][0] <= fuel:
        heapq.heappush(max_heap, -arr[index][1])
        index += 1

    if fuel >= L:
        print(answer)
        break

    if max_heap:
        fuel -= heapq.heappop(max_heap)
        answer += 1
    else:
        print(-1)
        break

# B. Bronze Cow Party
"""
import heapq

N,M,X = map(int,input().split())
graph = [[] for _ in range(N+1)]
distance = [101] * (N+1)
for _ in range(M):
    Ai,Bi,Ti = map(int,input().split())
    graph[Ai].append((Bi,Ti))
    graph[Bi].append((Ai,Ti))
q = []
heapq.heappush(q,(0,X))
distance[X] = 0
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for neighbor, weight in graph[now]:
        cost = dist + weight
        if cost < distance[neighbor]:
            distance[neighbor] = cost
            heapq.heappush(q, (cost, neighbor))
answer = 0
for i in range(1,N+1):
    answer = max(answer, distance[i])
print(answer*2)
"""
# C. 유럽여행
# 최소신장트리
"""
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N,P = map(int,input().split())
parents = [i for i in range(0,N+1)]
costs = [0] * (N+1)
for i in range(1,N+1):
    costs[i] = int(input())
edges = []
for _ in range(P):
    Sj,Ej,Lj = map(int,input().split())
    edges.append([Lj,Sj,Ej])
for edge in edges:
    edge[0] = (2*edge[0]) + costs[edge[1]] + costs[edge[2]]
edges.sort()

start = 1001
for i in range(1,N+1):
    start = min(start,costs[i])
for cost,a,b in edges:
    if find_parent(parents,a) != find_parent(parents,b):
        union_parent(parents,a,b)
        start += cost
print(start)
"""
# D. 젖짜기 스케줄링
"""
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int,input().split())
T = [0] * (N+1)
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
dp = [0] * (N+1)

for i in range(1,N+1):
    dp[i] = T[i] = int(input())
for i in range(1,M+1):
    A,B = map(int,input().split())
    indegree[B] += 1
    graph[A].append(B)

def topology_sort():
    q = deque()
    for i in range(1,N+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[i],dp[now] + T[i])
            if indegree[i] == 0:
                q.append(i)
topology_sort()
print(max(dp))
"""
# E. 겹치는 건 싫어
"""
N,K = map(int,input().split())
arr = list(map(int,input().split()))
count_dict = dict()
for c in arr:
    count_dict[c] = 0
end = 1
max_count = 0
max_length = 0
count_dict[arr[0]] = 1
for start in range(N-1):
    max_count = 0
    while end < N and max_count <= K:
        count_dict[arr[end]] += 1
        max_count = max(max_count, max(count_dict.values()))
        max_length = max(max_length, end - start)
        end += 1
    count_dict[arr[start]] -= 1
print(max_length)
"""
# F. 어두운 건 무서워
"""
M,N,Q = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(M)]

dp = [[0] * (N+1) for _ in range(M+1)]
for i in range(1,M+1):
    for j in range(1,N+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + graph[i-1][j-1]
for _ in range(Q):
    r1,c1,r2,c2 = map(int,input().split())
    light_sum = dp[r2][c2] - dp[r2][c1-1] - dp[r1-1][c2] + dp[r1-1][c1-1]
    c = (r2-r1+1) * (c2-c1+1)
    print(light_sum//c)
"""