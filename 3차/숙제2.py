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
# 숙제 4. 개인정보수집유효기간(WIP)
"""
def solution(today, terms, privacies):
    split_term = dict()
    for term in terms:
        type,date = term.split()
        split_term[type] = date

    for privacy in privacies:
        date,term = privacy.split()
        Year,month,day = map(int,date.split('.'))
        month += int(split_term[term])
        if(month > 12):
            month -= 12
            Year += 1
        print(Year,month,day)

    answer = []
    return answer
print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
# result [1,3]
print(solution("2020.01.01",["Z 3", "D 5"],["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
# result [1, 4, 5]
"""