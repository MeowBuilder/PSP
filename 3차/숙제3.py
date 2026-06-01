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








# 숙제 1. 두수의합
n = int(input())
L = list(map(int,input().split()))
x = int(input())
L.sort()
count = 0

for start in range(n):
    for end in range(start+1,n):
        if L[start] + L[end] == x:
            count += 1

print(count)