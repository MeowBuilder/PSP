# 실습. Quick_sort
"""
array = [5,7,9,0,3,1,6,2,4,8]
def quickSort(array):
    if len(array)<=1:
        return array
    pivot = array[0]
    tail = array[1:]
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quickSort(left_side) + [pivot] + quickSort(right_side)

print(quickSort(array))
"""

# 실습. 두 배열의 원소 교체
"""
N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort(reverse=True)

for i in range(K):
    if A[i] < B[i]:
        A[i],B[i] = B[i],A[i]
    else:
        break
print(sum(A))
"""
# 숙제 1. 주식투자
"""
T = int(input())
for _ in range(T):
    N = int(input())
    max_jusick = 0
    for d in range(N):
        A,B,C = map(int,input().split())
        if max(A,B,C) > 0:
            max_jusick += max(A,B,C)
    print(max_jusick)
"""
# 숙제 2. 회의실 배정
"""
N = int(input())
meeting_time = list()
for i in range(N):
    A,B = map(int,input().split())
    meeting_time.append((A,B))
meeting_time.sort(key=lambda x:(x[1],x[0]))

count = 0
last_end_time = 0
for i in range(N):
    if meeting_time[i][0] >= last_end_time:
        count += 1
        last_end_time = meeting_time[i][1]
print(count)
"""
# 숙제 3. 행렬 게임
"""
def print_matrix(MAT,mat_name):
    print(mat_name)
    for i in range(len(MAT)):
        for j in range(len(MAT[i])):
            if j+1 < len(MAT[i]):
                print(MAT[i][j],end=' ')
            else:
                print(MAT[i][j])

A,B = map(int,input().split())
matrix = [[(B*j)+(i+1) for i in range(B)] for j in range(A)]
print_matrix(matrix,'M')
Right = [[matrix[(A-1)-j][i] for j in range(A) ] for i in range(B)]
print_matrix(Right,'R')
Left = [[matrix[j][(B-1)-i]for j in range(A)] for i in range(B)]
print_matrix(Left,'L')
Trans = [[matrix[j][i]for j in range(A)] for i in range(B)]
print_matrix(Trans,'T')
"""
"""
# 교수님 풀이
A,B = map(int,input().split())
M = [[r*B + c+1 for c in range(B)] for r in range(A)]
print_matrix(M,'M')
R = [[M[r][c] for r in range(A-1,-1,-1)]for c in range(B)]
print_matrix(R,'R')
L = [[M[r][c] for r in range(A)] for c in range(B-1,-1,-1)]
print_matrix(L,'L')
T = [[M[r][c] for r in range(A)] for c in range(B)]
print_matrix(T,'T')
"""
# 숙제 4. 실패율
"""
def solution(N, stages):
    P = [0] * (N+2) # 각 스테이지에 도달한 사람수
    F = [0] * (N+2) # 각 스테이지에 실패한 사람수
    R = []          # 각 스테이지의 (실패율, 스테이지 번호)
    for s in stages:
        for i in range(1,s+1):
            P[i] += 1
        F[s] += 1
    for i in range(1,N+1):
        if P[i] == 0:
            R.append((0,i))
        else:
            R.append((F[i]/P[i],i))
    R.sort(key=lambda x: (-x[0],x[1]))
    answer = [R[i][1] for i in range(N)]
    return answer

print(solution(5,[2,1,2,6,2,4,3,3]))
print(solution(4,[4,4,4,4,4]))
"""
# 숙제 5. 소가 길을 건너간 이유 3
"""
N = int(input())
cows = [list(map(int,input().split())) for _ in range(N)]

cows.sort()

cur_time = 0
for i in range(N):
    if cur_time < cows[i][0]:   # 도착한 소가 없으면
        cur_time = cows[i][0]   # 소가 도착할 때까지 시간이 흐름
    cur_time += cows[i][1]      # 검사시간 만큼 시간이 흐름

print(cur_time)
"""
"""
# 교수님 풀이
clock = 0
for arr_time, check_time in cows:
    if arr_time > clock:
        clock = arr_time
    clock += check_time
print(clock)
"""