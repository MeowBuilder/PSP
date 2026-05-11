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
# 숙제 2. 순회강연