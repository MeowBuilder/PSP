# 실습. 1이 될때까지
"""
N,K = map(int,input().split())
count = 0
while N > 1:
    if N % K == 0:
        N //= K
        count += 1
    else:
        N -= 1
        count += 1
print(count)
"""
from turtledemo.penrose import start

"""
N,K = map(int,input().split())
count = 0
while N > 1:
    target = (N//K)*K
    count += (N-target)
    N = target
    if N < K: break
    count += 1
    N //= K
count += (N - 1)
print(count)
"""
# 실습. 곱하기 혹은 더하기
"""
num_list = input()
result = 0
for c in num_list:
    num = int(c)
    if num <= 1 or result <= 1: result += num
    else: result *= num
print(result)
"""
# 실습. 모험가 길드
"""
Traveler = int(input())
Fear = list(map(int,input().split()))
Fear.sort()

result = 0
count = 0

for Person in Fear:
    count += 1
    if count >= Person:
        result += 1
        count = 0

print(result)
"""
# 실습. 상하좌우
"""
Board_SIZE = int(input())
Plans = input().split()
r,c = 1,1

dr = [-1,1,0,0]
dc = [0,0,-1,1]
move_types = ['L','R','U','D']

for plan in Plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nr = r + dr[i]
            nc = c + dc[i]
    if nc < 1 or nr < 1 or nc > Board_SIZE or nr > Board_SIZE:
        continue
    r,c = nr,nc
print(r,c)
"""
# 실습. 왕실의 나이트
"""
data = input()
r = int(data[1])
c = ord(data[0]) - ord('a') + 1
result = 0
for dr,dc in [[-2,-1],[-2,1],[-1,-2],[-1,2],[2,-1],[2,1],[1,-2],[1,2]]:
    nr,nc = r+dr,c+dc
    if 1 <= nr <= 8 and 1 <= nc <= 8:
        result += 1
print(result)
"""
# 실습. 시각
"""
Input = int(input())
count = 0
for i in range(Input+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)
"""
# 실습. 문자열 재정렬
"""
Input = input()
Output_str = []
Output_sum = 0
for c in Input:
    if c.isdigit():
        Output_sum += int(c)
    else:
        Output_str.append(c)
Output_str.sort()
if Output_sum != 0:
    Output_str.append(str(Output_sum))
print(''.join(Output_str))
"""
#숙제 1. 백준 동전 0
"""
N,K = map(int,input().split())

Change_array = [int(input()) for _ in range(N)]
Change_array.reverse()

count = 0
for coin in Change_array:
    count += K // coin
    K %= coin

print(count)
"""

#숙제 2. 백준 블랙잭
"""
from itertools import combinations
N,M = map(int,input().split())
card = list(map(int,input().split()))
Max = 0
for c in combinations(card,3):
    if sum(c) <= M:
        Max = max(Max,sum(c))
print(Max)
"""

#숙제 3. TUKorea 자산증감 (Joat)
Day = int(input())
Input = input()
Answer = [['.'] * Day]
r = 0
for i in range(Day):
    char = Input[i]
    if char == '+':
        if i > 0 and Input[i - 1] == '+':
            r -= 1
    elif char == '-':
        if i > 0 and Input[i - 1] == '-':
            r += 1
        elif i > 0 and Input[i - 1] == '=':
            r += 1
    elif char == '=':
        if r > 0 and Input[i - 1] == '+':
            r -= 1

    if r < 0:
        Answer.insert(0, ['.' for _ in range(Day)])
        r = 0
    elif r >= len(Answer):
        Answer.append(['.' for _ in range(Day)])
        r = len(Answer) - 1

    draw_char = '/' if char == '+' else '\\' if char == '-' else '_'
    Answer[r][i] = draw_char

for row in Answer:
    print("".join(row))

#숙제 4. TUKorea 균형 잡힌 영양소
# 더럽지만 일단 통과
"""
from itertools import combinations
N = int(input())
Food = []
for i in range(N):
    T,D,G = map(int,input().split())
    Cal = T*4 + D*4 + G*9
    Food.append([T,D,G,Cal])
gizun = list(map(int,input().split()))
count = 0
for i in range(1,4):
    for c in combinations(Food,i):
        T_sum = 0
        D_sum = 0
        G_sum = 0
        cal_sum = 0
        for F in c:
            T_sum += F[0]
            D_sum += F[1]
            G_sum += F[2]
            cal_sum += F[3]
        if T_sum <= gizun[0] and D_sum >= gizun[1] and G_sum <= gizun[2] and cal_sum <= gizun[3]:
            count += 1
print(count)
"""
# 교수님 풀이
"""
from itertools import combinations
N = int(input())
Food = [list(map(int,input().split())) for _ in range(N)]
gizun = list(map(int,input().split()))
result = 0
for i in range(1,4):
    if i > N: break
    for food_comb in combinations(Food,i):
        T_sum, D_sum, G_sum, cal_sum = 0,0,0,0
        for F in food_comb:
            T_sum += F[0]
            D_sum += F[1]
            G_sum += F[2]
            cal_sum += F[0] * 4 + F[1] * 4 + F[2] * 9
        if T_sum <= gizun[0] and D_sum >= gizun[1] and G_sum <= gizun[2] and cal_sum <= gizun[3]:
            result += 1
print(result)
"""
#숙제 5. 프로그래머스 체육복
""" # 내 풀이
def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    left = lost[:]
    for c in lost:
        if c in reserve:
            reserve.remove(c)
            left.remove(c)
    lost = left[:]
    for i in left:
        if i-1 in reserve:
            lost.remove(i)
            reserve.remove(i-1)
        elif i+1 in reserve:
            lost.remove(i)
            reserve.remove(i+1)

    return n - len(lost)

print(solution(5,[2,4],[1,3,5]))
print(solution(5,[2,4],[3]))
print(solution(3,[3],[1]))
"""
""" # 교수님 답안
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    _reserve.sort()
    for r in _reserve:
        if r - 1 in _lost:
            _lost.remove(r - 1)
        elif r + 1 in _lost:
            _lost.remove(r + 1)
    return n - len(_lost)

print(solution(5,[2,4],[1,3,5]))
print(solution(5,[2,4],[3]))
print(solution(3,[3],[1]))
"""