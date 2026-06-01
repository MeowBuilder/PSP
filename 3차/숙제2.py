# 서로소 집합 자료구조
# 최소 신장 트리 (Minimum Spanning Tree) - 크루스칼 (Kruskal)
"""
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
"""

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
"""
"""
v,e = map(int,input().split())
parents = [i for i in range(0,v+1)]
edges = []
result = 0
for _ in range(e):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))
edges.sort()

for cost,a,b in edges:
    if find_parent(parents,a) != find_parent(parents,b):
        union_parent(parents,a,b)
        result += cost
print(result)
"""
# 위상 정렬
"""
'''
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
'''
from collections import deque
v,e = map(int,input().split())
indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    q = deque()
    result = []
    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in result:
        print(i,end=' ')

topology_sort()
"""
# 숙제 1. 도시분할계획
"""
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N,M = map(int,input().split())
parent = [i for i in range(0,N+1)]
edges = []
for _ in range(M):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))
edges.sort()
sum_cost = 0
max_cost = 0
for cost,a,b in edges:
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        max_cost = max(cost,max_cost)
        sum_cost += cost
print(sum_cost-max_cost)
"""
# 숙제 2. 선수과목
"""
from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1

answer = [0] * (N+1)

q = deque()
for i in range(1,N+1):
    if indegree[i] == 0:
        q.append(i)
        answer[i] = 1
while q:
    now = q.popleft()
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            answer[i] = answer[now] + 1
            q.append(i)
for i in range(1,N+1):
    print(answer[i],end=' ')
"""
# 숙제 3. 작업
"""
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
indegree = [0] * (N+1)
T = [0] * (N+1)
graph = [[] for _ in range(N+1)]
# dp[i] : i번 작업까지의 최소 수행시간
dp = [0] * (N+1)
for i in range(1,N+1):
    in_array = list(map(int,input().split()))
    dp[i] = T[i] = in_array[0]
    indegree[i] = in_array[1]
    for j in in_array[2:]:
        graph[j].append(i)

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
# 숙제 4. 개인정보수집유효기간(WIP)

def solution(today, terms, privacies):
    split_term = dict()
    now = list(map(int,today.split('.')))
    answer = []

    for term in terms:
        type,days = term.split()
        split_term[type] = days

    for i in range(len(privacies)):
        date,term = privacies[i].split()
        month = int(split_term[term])
        Year,Month,Day = map(int,date.split('.'))
        Month += month
        if Month > 12:
            Month -= 12
            Year += 1
        if now[0] > Year:
            answer.append(i+1)
        elif now[0] == Year and now[1] > Month:
            answer.append(i+1)
        elif now[0] == Year and now[1] == Month and now[2] >= Day:
            answer.append(i+1)
    return answer
print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.06.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
# result [1,3]
print(solution("2020.01.01",["Z 3", "D 5"],["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
# result [1, 4, 5]
