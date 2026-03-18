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
# 틀림
N,M = map(int,input().split())
card = list(map(int,input().split()))
MAX_list = []
i = 0
Max = 0
card_id = 0
while i < N:
    if Max + card[card_id] <= M:
        Max += card[card_id]
        card_id += 1
    else:
        card_id += 1

    if card_id >= N:
        MAX_list.append(Max)
        Max = 0
        card_id = 0
        i += 1
print(max(MAX_list))

#숙제 3. 백준


#숙제 4. 백준


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