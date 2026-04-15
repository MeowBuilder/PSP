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
def print_matrix(MAT):
    for i in range(len(MAT)):
        for j in range(len(MAT[i])):
            if j+1 < len(MAT[i]):
                print(MAT[i][j],end=' ')
            else:
                print(MAT[i][j])

A,B = map(int,input().split())
matrix = [[(B*j)+(i+1) for i in range(B)] for j in range(A)]
print('M')
print_matrix(matrix)
print('R')
Right = [[matrix[(A-1)-j][i] for j in range(A) ] for i in range(B)]
print_matrix(Right)
print('L')
Left = [[matrix[j][(B-1)-i]for j in range(A)] for i in range(B)]
print_matrix(Left)
print('T')
Trans = [[matrix[j][i]for j in range(A)] for i in range(B)]
print_matrix(Trans)
"""
# 숙제 4. 실패율