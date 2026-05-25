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
"""
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
# 숙제 3. 소가길을건너간이유4
"""
C,N = map(int,input().split())
T = [int(input()) for _ in range(C)]
A = [list(map(int,input().split())) for _ in range(N)]
T.sort()
A.sort(key=lambda x:x[0])
#print(T)
# [2, 6, 7, 8, 9]
#print(A)
# [[8, 13], [4, 9], [2, 5], [0, 3]]
answer = 0
cow_index = 0
min_heap = []
for time in T:
    while cow_index < N and A[cow_index][0] <= time:
        heapq.heappush(min_heap, A[cow_index][1])
        cow_index += 1
    while min_heap and min_heap[0] < time:
        heapq.heappop(min_heap)
    
    if min_heap:
        heapq.heappop(min_heap)
        answer += 1
print(answer)
"""
# 숙제 4. 다음 순열
"""
N,K = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(K)]
    
def next_permutation(arr):
    i = len(arr) - 1
    while i > 0 and arr[i-1] >= arr[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(arr) - 1
    while arr[j] <= arr[i-1]:
        j -= 1
    arr[i-1], arr[j] = arr[j], arr[i-1]
    arr[i:] = reversed(arr[i:])
    return True

for i in range(K):
    next_permutation(array[i])
    print(*array[i],end= ' \n')
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
# 숙제 7. 장애물
'''
sample input
5 7
2 1 5
1 3 1
3 2 8
3 5 7
3 4 3
2 4 7
4 5 2
sample output
2
'''
def dijkstra(start, V, graph, double_edge=None):
    distances = [INF] * (V + 1)
    parent = [0] * (V + 1)
    
    distances[start] = 0
    queue = [(0, start)]
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if distances[current_node] < current_distance:
            continue
            
        for neighbor, weight in graph[current_node]:
            if double_edge and ((current_node == double_edge[0] and neighbor == double_edge[1]) or 
                                (current_node == double_edge[1] and neighbor == double_edge[0])):
                next_weight = weight * 2
            else:
                next_weight = weight
                
            distance = current_distance + next_weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parent[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))
                
    return distances, parent

V,E = map(int,input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
orig_distance, parent = dijkstra(1, V, graph)
A = orig_distance[V]

path_edges = []
curr = V
while curr != 1:
    prev = parent[curr]
    path_edges.append((prev, curr))
    curr = prev

max_diff = 0
for edge in path_edges:
    double_distance, _ = dijkstra(1, V, graph, double_edge=edge)
    B = double_distance[V]
    if B != INF:
        max_diff = max(max_diff, B - A)
        
print(max_diff)
