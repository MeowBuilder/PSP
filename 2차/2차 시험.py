"""
# 2 + 1 세일
N = int(input())
array = [int(input()) for _ in range(N)]

array.sort(reverse=True)
money = 0
count = 0
for i in range(N):
    money += array[i]
    count += 1
    if count % 3 == 0:
        money -= array[i]
print(money)
"""
"""
# 눈송이
P = int(input())
for _ in range(P):
    n,m = map(int,input().split())
    array = [input() for _ in range(n)]
    max_size = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] == '+':
                r,c = i,j
                size = 0
                leng = 1
                B = True
                while True:
                    for dir in [(-leng,0,45),(leng,0,45),(0,-leng,124),(0,leng,124),
                                (-leng,-leng,92),(leng,-leng,47),(-leng,leng,47)
                        ,(leng,leng,92  )]:
                        nr,nc = r+dir[0],c+dir[1]
                        if 0 <= nr < n and 0 <= nc < m and ascii(array[nr][nc]) == dir[2]:
                            B = False
                            continue
                        else:
                            B = True
                            break
                    if B: break
                    leng += 1
                    size += 1
                max_size = max(max_size,size)
    print(max_size)
"""



"""
# 7Krokod 게임
from itertools import combinations_with_replacement
n,m = map(int,input().split())
array = input()

def Get_point(array):
    words_copy = array.copy()
    point = 0
    for word in words_copy:
        point += words_copy[word] * words_copy[word]
    while words_copy['k'] >= 2 and words_copy['o'] >= 2 and words_copy['r'] >= 1 and words_copy['d'] >= 1:
        point += 7
        words_copy['k'] -= 2
        words_copy['o'] -= 2
        words_copy['r'] -= 1
        words_copy['d'] -= 1
    return point

words = dict()
for word in array:
    if word not in words:
        words[word] = 1
    else:
        words[word] += 1

answer = 0
if m >= 1:
    for comb in combinations_with_replacement(words,m):
        for i in comb:
            words[i] += 1
        answer = max(answer,Get_point(words))
        for i in comb:
            words[i] -= 1
else:
    answer = Get_point(words)
print(answer)
"""
"""
# 격자상의 경로
N,M,K = map(int,input().split())
Map = [[0]*(M) for _ in range(N)]
if K == 0:
    for i in range(0, N):
        for j in range(0, M):
            if i == 0 and j == 0:
                Map[i][j] = 1
            else:
                Map[i][j] = Map[i - 1][j] + Map[i][j - 1]
else:
    first_n = K // M
    first_m = K % M
    for i in range(0,first_n+1):
        for j in range(0,first_m):
            if i == 0 and j == 0:
                Map[i][j] = 1
            else:
                Map[i][j] = Map[i-1][j] + Map[i][j-1]
    for i in range(first_n,N):
        for j in range(first_m-1,M):
            Map[i][j] = Map[i-1][j] + Map[i][j-1]
print(Map[N-1][M-1])
"""

# 점프
N = int(input())
array = [list(map(int,input().split())) for _ in range(N)]
dp = [[0] * (N) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            dp[i][j] = 1
        if dp[i][j] != 0:
            move = array[i][j]
            for k in [(i+move,j),(i,j+move)]:
                if k[0] < N and k[1] < N:
                    dp[k[0]][k[1]] += dp[i][j]

print(dp[N-1][N-1])
