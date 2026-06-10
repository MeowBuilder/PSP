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
# 숙제 4. 개인정보수집유효기간
"""
def solution(today, terms, privacies):
    answer = []
    
    # 날짜를 총 '일(day)' 수로 바꿔주는 변환 함수
    def to_days(date_str):
        y, m, d = map(int, date_str.split('.'))
        return (y * 12 * 28) + (m * 28) + d

    # 1. 오늘 날짜를 일 수로 변환
    today_days = to_days(today)
    
    # 2. 약관 종류별 유효기간 저장 (달 수 -> 일 수로 바로 변환해서 저장)
    term_dict = {}
    for term in terms:
        t_type, t_month = term.split()
        term_dict[t_type] = int(t_month) * 28  # 1달 = 28일
        
    # 3. 개인정보 만료 여부 확인
    for i, privacy in enumerate(privacies):
        p_date, p_type = privacy.split()
        
        # (수집된 날의 총 일수) + (약관 유효 기간 일수) = 만료되는 날(이 날부터 파기)
        expire_days = to_days(p_date) + term_dict[p_type]
        
        # 오늘 날짜가 만료일과 같거나 지났다면 파기 대상
        if today_days >= expire_days:
            answer.append(i + 1)
            
    return answer
"""
# 숙제 5. 신규 아이디 추천

def solution(new_id):
    new_id = new_id.lower()
    
    answer = ""
    for char in new_id:
        if char.isalnum() or char in ['-', '_', '.']:
            answer += char
            
    while '..' in answer:
        answer = answer.replace('..', '.')

    if answer and answer[0] == '.':
        answer = answer[1:]
    if answer and answer[-1] == '.':
        answer = answer[:-1]
        
    if answer == '':
        answer = 'a'
        
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
            
    while len(answer) < 3:
        answer += answer[-1]
        
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))