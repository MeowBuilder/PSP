# 피보나치 함수 재귀 -> 다이나믹 프로그래밍
"""
#탑다운
dp = [0] * 1000
def fibo(x):
    if x == 1 or x == 2:
        return 1
    if dp[x] != 0:
        return dp[x]
    dp[x] = fibo(x - 1) + fibo(x - 2)
    return dp[x]
print(fibo(1000))
"""

"""
# 바텀업
dp = [0]*1001
dp[1] = dp[2] = 1
for i in range(3, 1001):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[1000])
"""
# 실습 개미 전사
"""
N = int(input())
L = list(map(int, input().split()))
dp = [0] * (N+1)
dp[0] = L[0]
dp[1] = max(L[0], L[1])
for i in range(2, N):
    dp[i] = max(dp[i-1],dp[i-2] + L[i])
print(dp[N-1])
"""
# 실습 1로 만들기
"""
X = int(input())
dp = [0] * (X+1)

for i in range(2, X+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i//5] + 1)

print(dp[X])
"""
# 실습 효율적인 화폐 구성
"""
N,M = map(int, input().split())
L = [int(input()) for _ in range(N)]
dp = [10001] * (M+1)
dp[0] = 0
for i in range(N):
    for j in range(L[i],M+1):
        if dp[j - L[i]] != 10001:
            dp[j] = min(dp[j],dp[j-L[i]]+1)
if dp[M] == 10001:
    print(-1)
else:
    print(dp[M])
"""
# 실습 금광
"""
for tc in range(int(input())):
    n,m = map(int, input().split())
    List = list(map(int, input().split()))
    cave = []
    index = 0
    for i in range(n):
        cave.append(List[index:index+m])
        index += m
    for j in range(1,m):
        for i in range(n):
            if i == 0: left_up = 0
            else: left_up = cave[i-1][j-1]

            if i == n - 1: left_down = 0
            else: left_down = cave[i+1][j-1]

            left = cave[i][j-1]
            cave[i][j] = cave[i][j]+max(left_up,left_down,left)
    result = 0
    for i in range(n):
        result = max(result,cave[i][m-1])
    print(result)
"""
# 숙제 1. 정수삼각형
"""
# 탑다운
def solution(triangle):
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0: Left = 0
            else: Left = triangle[i-1][j-1]

            if j == len(triangle[i])-1: Right = 0
            else: Right = triangle[i-1][j]

            triangle[i][j] = triangle[i][j] + max(Left, Right)
    answer = 0
    for i in range(len(triangle[len(triangle)-1])):
        answer = max(answer,triangle[len(triangle)-1][i])
    return answer
print(solution([[7],[3,8],[8,1,0],[2,7,4,4],[4,5,2,6,5]]))
"""
"""
# 바텀업 (교수님 풀이)
def solution(triangle):
    L = len(triangle)
    for i in range(L-2,-1,-1):
        for j in range(len(triangle[i])):
            triangle[i][j] = triangle[i][j] + max(triangle[i+1][j],triangle[i+1][j+1])
    return triangle[0][0]
print(solution([[7],[3,8],[8,1,0],[2,7,4,4],[4,5,2,6,5]]))
"""
# 숙제 2. 등굣길
"""
def solution(m, n, puddles):
    dp = [[0]*(m+1) for _ in range(n+1)]
    puddleList = [[0]*(m+1) for _ in range(n+1)]
    for c,r in puddles:
        puddleList[r][c] = 1
    for r in range(1,n+1):
        for c in range(1,m+1):
            if r == 1 and c == 1:
                dp[r][c] = 1
            elif puddleList[r][c] == 1:
                dp[r][c] = 0
            else:
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
    return dp[n][m] % 1000000007
print(solution(4,3,[[2,2]]))
"""
# 숙제 5. 도둑질
"""
#dp0[i] : 0~L-2
#dp1[i] : 1~L-1
def solution(money):
    L = len(money)
    dp0 = [0] * L
    dp0[0] = money[0]
    dp0[1] = max(money[0], money[1])
    for i in range(2,L-1):
        dp0[i] = max(dp0[i-1],dp0[i-2] + money[i])

    dp1 = [0] * L
    dp1[1] = money[1]
    for i in range(2, L):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])

    return max(dp0[L-2], dp1[L-1])
print(solution([1,2,3,1]))
"""
# 숙제 6. 설탕배달
# 이 유형은 내가 옮기려는 무게(i)에서 선택한 포대의 무게(k)만큼
# 뺀 무게의 운반횟수(dp[i-k])에서 +1 한 값(6kg 운반은 3kg 운반 + 3kg운반)과
# 기존의 최솟값을 비교해 dp를 업데이트
# 0kg 운반에는 0포대 필요 dp[0] = 0
# 점화식
# 모든 k 에 대해서 dp[i-k]가 INF가 아니면, dp[i] = min(dp[i],dp[i-k]+1)
"""
N = int(input())
dp = [5001] * (N+1)
dp[0] = 0
for k in [3,5]: # 3,5kg포대를 사용한다
    for i in range(k,N+1): # 목표 무게까지 반복
        if dp[i-k] != 5001: # 포대 무게를 뺀 만큼 운반
            dp[i] = min(dp[i],dp[i-k]+1) # 기존 최솟값과 비교
if dp[N] == 5001:
    print(-1)
else:
    print(dp[N])
"""
# 숙제 7. 1로 만들기
"""
N = int(input())
dp = [0] * (N+1)
for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
print(dp[N])
"""
# 숙제 8. 내려가기
"""
# 메모리 초과 안걸리게
N = int(input())
dp_max = list(map(int, input().split()))
dp_min = dp_max[:]
for _ in range(N-1):
    array = list(map(int, input().split()))
    p_max = [None] * 3
    p_min = [None] * 3
    for c in range(3):
        if c == 0: up_left_max = 0; up_left_min = 1e12
        else: up_left_max = dp_max[c-1]; up_left_min = dp_min[c-1]

        if c == 2: up_right_max = 0; up_right_min = 1e12
        else: up_right_max = dp_max[c+1]; up_right_min = dp_min[c+1]

        up_max = dp_max[c]; up_min = dp_min[c]
        p_max[c] = array[c]+max(up_left_max,up_right_max,up_max)
        p_min[c] = array[c]+min(up_left_min,up_right_min,up_min)
    dp_max = p_max[:]
    dp_min = p_min[:]
print(max(dp_max),min(dp_min))
"""