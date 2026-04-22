# 이진 탐색 반복문 구현
"""
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n, target = map(int, input().split())
array = list(map(int, input().split()))
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1,'번째 원소')
"""
# 특정 범위 데이터 개수 구하기
"""
from bisect import bisect_left, bisect_right

def count_by_range(a,left_value,right_value):
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a,left_value)
    return right_index - left_index

a = [1,2,3,3,3,3,4,4,8,9]

print(count_by_range(a,4,4))
print(count_by_range(a,-1,3))
"""
# 숙제 1. 나무 자르기
"""
N,M = map(int, input().split())
array = list(map(int, input().split()))

def check(mid):
    total = 0
    for x in array:
        if x > mid:
            total += x - mid
    return total >= M

start = 0
end = max(array)
result = 0
while start <= end:
    mid = (start + end) // 2
    if check(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)
"""
# 숙제 2. 사칙연산
"""
T = int(input())
for _ in range(T):
    a,b = input().split('=')
    if eval(a) == eval(b):
        print('correct')
    else:
        print('wrong answer')
"""
# 숙제 3. Postfix 표현식
"""
from collections import deque

postfix = input()
stack = deque()
for c in postfix:
    if c == '+' or c == '-':
        a = stack.pop()
        b = stack.pop()
        fixed = f'({b+c+a})'
        stack.append(fixed)
    else:
        stack.append(c)
print(''.join(stack))
"""
"""
postfix = input()
S = []
for c in postfix:
    if c.isalpha():
        S.append(c)
    else:
        a = S.pop()
        b = S.pop()
        fixed = f'({b+c+a})'
        S.append(fixed)
print(S.pop())
"""
# 숙제 4. 비밀지도
# int to binary
# print(list(bin(int(input())).replace('0b', '')))
def solution(n, arr1, arr2):
    array = [['' for _ in range(n)] for _ in range(n)]
    for i in range(len(arr1)):
        bin_code = bin(arr1[i]).replace('0b', '')[::-1]
        print(bin_code)
        for x in range(n):
            pass
    return array
print(solution(5,[9,20,28,18,11],[30, 1, 21, 17, 28]))
# ["#####","# # #", "### #", "# ##", "#####"]
print(solution(5,[46, 33, 33 ,22, 31, 50],	[27 ,56, 19, 14, 14, 10]))
# ["######", "### #", "## ##", " #### ", " #####", "### # "]

# 숙제 5. 어두운 굴다리
"""
N = int(input())
M = int(input())
array = list(map(int, input().split()))

def check(mid):
    point = 0
    for x in array:
        if x - mid > point:
            return False
        point = x + mid
    if point >= N:
        return True
    else:
        return False

start = 1
end = N
result = 0
while start <= end:
    mid = (start + end) // 2
    if check(mid):
        result = mid
        end = mid - 1
    else:
        start = mid + 1
print(result)
"""