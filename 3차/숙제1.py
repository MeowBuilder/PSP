import heapq
import sys
input = sys.stdin.readline
INF = 1e9
# 다익스트라 실습
"""
'''
6 11
1
1 2 2
1 3 5
1 4 1
2 4 2
2 3 3
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''
n,m = map(int,input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for neighbor, weight in graph[now]:
            cost = dist + weight
            if cost < distance[neighbor]:
                distance[neighbor] = cost
                heapq.heappush(q, (cost, neighbor))

dijkstra(start)
print(distance)
"""
# 숙제 1. 택배 배송
"""
N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for neighbor, weight in graph[now]:
            cost = dist + weight
            if cost < distance[neighbor]:
                distance[neighbor] = cost
                heapq.heappush(q, (cost, neighbor))

dijkstra(1)
print(distance[N])
"""
"""
# 숙제 2. 순회강연
n = int(input())
tasks = [list(map(int,input().split())) for _ in range(n)]
tasks.sort(key=lambda x:-x[1]) # 내림차순 정렬, reverse=True 대신 숫자인 경우 -x로 가능함
max_heap = []
answer = 0
index = 0
for day in range(10000,0,-1):
    while index < n and tasks[index][1] == day:
        heapq.heappush(max_heap,-tasks[index][0])
        index += 1
    if max_heap:
        answer -= heapq.heappop(max_heap)
print(answer)
"""
"""
# 숙제 3. 소가길을건너간이유4
C,N = map(int,input().split())
T = [int(input()) for _ in range(C)]
A = [list(map(int,input().split())) for _ in range(N)]
T.sort(reverse=True)
A.sort(key=lambda x:-x[1])
#print(T)
# [9, 8, 7, 6, 2]
#print(A)
# [[8, 13], [4, 9], [2, 5], [0, 3]]
"""
# 숙제 5. 합승 택시
"""
# 다익스트라 버전
def dijkstra(start,graph,n):
    distance = [INF] * (n+1)
    distance[start] = 0
    q = [(0, start)]
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: continue
        for adj, weight in graph[now]:
            cost = dist + weight
            if cost < distance[adj]:
                distance[adj] = cost
                heapq.heappush(q, (cost, adj))
    return distance

def solution(n, s, a, b, fares):#노드 수,출발지점,A 도착지, B도착지, 지점 사이 예상 택시요금
    graph = [[] for _ in range(n+1)]
    for u,v,w in fares:
        graph[u].append((v,w))
        graph[v].append((u,w))
    dist_s = dijkstra(s,graph,n)
    dist_a = dijkstra(a,graph,n)
    dist_b = dijkstra(b,graph,n)
    answer = INF
    for k in range(1,n+1):
        answer = min(answer,dist_s[k] + dist_a[k] + dist_b[k])
    return answer
"""
"""
# 플루이드 워셜
def solution(n, s, a, b, fares):#노드 수,출발지점,A 도착지, B도착지, 지점 사이 예상 택시요금
    distance = [[INF] * (n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        distance[i][i] = 0
    for u,v,w in fares:
        distance[u][v] = w
        distance[v][u] = w
    # Floyd Warshall
    # 3중 루프, i = 시작점, j = 도착점, k = 거쳐가는점
    for k in range(1,n+1): # 반드시 거쳐가는 점 k가 가장 바깥에
        for i in range(1,n+1):
            for j in range(1,n+1):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    answer = INF
    for k in range(1,n+1):
        answer = min(answer,distance[s][k] + distance[k][a] + distance[k][b])
    return answer

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
# result : 82
print(solution(7,3,4,1,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
# result : 14
print(solution(6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))
# result : 18
"""
# 숙제 6. 파티
"""
def dijkstra(start, graph):
    distance = [INF] * (N+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: continue
        for adj, weight in graph[now]:
            cost = dist + weight
            if cost < distance[adj]:
                distance[adj] = cost
                heapq.heappush(q, (cost, adj))
    return distance

N,M,X = map(int,input().split())
graph = [[] for _ in range(N+1)]
rev_graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    rev_graph[b].append((a,c))

dist_from_X = dijkstra(X,graph)
dist_to_X = dijkstra(X,rev_graph)
max_dist = 0
for i in range(1,N+1):
    max_dist = max(max_dist, dist_from_X[i] + dist_to_X[i])
print(max_dist)
"""
"""
# 내 풀이
distance = [INF] * (N+1)
rev_distance = [INF] * (N+1)
def dijkstra(start,graph_array,dist_array):
    q = []
    heapq.heappush(q, (0, start))
    dist_array[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist_array[now] < dist:
            continue
        for neighbor, weight in graph_array[now]:
            cost = dist + weight
            if cost < dist_array[neighbor]:
                dist_array[neighbor] = cost
                heapq.heappush(q, (cost, neighbor))
dijkstra(X,graph,distance)
dijkstra(X,rev_graph,rev_distance)
answer = []
for i in range(1,N+1):
    answer.append(distance[i] + rev_distance[i])
print(max(answer))
"""
