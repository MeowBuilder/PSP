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

# 숙제 5. 설탕배달
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
# 숙제 6. 1로 만들기
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
