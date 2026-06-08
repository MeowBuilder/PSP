# 소수의 판별
"""
import math
def is_prime_number(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
"""
# 에라토스테네스의 체 알고리즘
"""
N = int(input())
array = [True for i in range(N+1)]
for i in range(2,int(math.sqrt(N))+1):
    if array[i] == True:
        j = 2
        while i*j <= N:
            array[i*j] = False
            j += 1
for i in range(2,N+1):
    if array[i]:
        print(i, end=' ')
"""
# 투 포인터
"""
n,m = 5,5
data = [1,2,3,2,5]

count = 0
interval_sum = 0
end = 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]
print(count)
"""
# 구간 합/접두사 합
"""
n = 5
data = [10,20,30,40,50]

dp = [0] * (n+1)
for i in range(1,n+1):
    dp[i] = dp[i-1] + data[i-1]

left = 3
right = 4
print(dp[right] - dp[left-1])
"""



# 숙제 1. 두수의합
"""
n = int(input())
L = list(map(int,input().split()))
x = int(input())
L.sort()

count = 0
end = 1

for start in range(n-1):
    if start == end:
        end += 1
    while L[start] + L[end] < x and end < n-1:
        end += 1
    while L[start] + L[end] > x and start+1 < end:
        end -= 1
    if L[start] + L[end] == x:
        count += 1

print(count)
"""
# 숙제 2. 소수회문
"""
import math
def is_prime_number(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
def is_palindrome(n):
    return str(n) == str(n)[::-1]
N = int(input())
while True:
    if is_palindrome(N) and is_prime_number(N):
        print(N)
        break
    N += 1
"""
# 숙제 3. b진법(WIP)
b,N,M = map(int,input().split())
N_L = list(map(int,input().split()))
N_L = N_L[::-1]
M_L = list(map(int,input().split()))
M_L = M_L[::-1]
N_ten = 0
M_ten = 0
for i in range(len(N_L)):
    N_ten += N_L[i] * b**i
for i in range(len(M_L)):
    M_ten += M_L[i] * b**i
answer = N_ten * M_ten


# 숙제 4. 목재총량
"""
M,N = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(M)]

dp = [[0] * (N+1) for _ in range(M+1)]
for i in range(1,M+1):
    for j in range(1,N+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + graph[i-1][j-1]

C = int(input())
for _ in range(C):
    r1,c1,r2,c2 = map(int,input().split())
    print(dp[r2][c2] - dp[r2][c1-1] - dp[r1-1][c2] + dp[r1-1][c1-1])
"""