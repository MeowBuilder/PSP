#숙제 1. 백준 하얀칸
"""
flag = True
count = 0

for _ in range(8):
    L = input()
    for i in range(8):
        if flag:
            if i % 2 == 0 and L[i] == 'F':
                count += 1
        else:
            if i % 2 == 1 and L[i] == 'F':
                count += 1
    flag = not flag

print(count)
"""
from unicodedata import digit

#숙제 2. 백준 ACM 호텔
""" 
Data_count = int(input())

for _ in range(Data_count):
    H,W,N = map(int,input().split())
    count = 0
    for w in range(1,W+1):
        for h in range(1,H+1):
            count += 1
            if count == N:
                print(h*100 + w)
                break
"""

#숙제 3. 백준 오셀로 재배치
"""
Data_count = int(input())

for _ in range(Data_count):
    Piece_count = int(input())
    Start = input()
    End = input()
    WtB = 0
    BtW = 0
    for i in range(Piece_count):
        if Start[i] == 'W' and End[i] == 'B':
            WtB += 1
        elif Start[i] == 'B' and End[i] == 'W':
            BtW += 1
    print(max(WtB,BtW))
"""

#숙제 4. TUKorea 문자열 폭발
"""
Data = input()
Explosive = input()
while Data.find(Explosive) != -1:
    Data = Data.replace(Explosive,'')
print(Data)
"""

#숙제 5. TUKorea 십자말 풀이
"""
[A,B] = input().split()
answer = [["."] * len(A) for _ in range(len(B))]

for c in range(len(A)):
    r = B.find(A[c])
    if r != -1:
        break

for i in range(len(A)):
    answer[r][i] = A[i]
for i in range(len(B)):
    answer[i][c] = B[i]

for r in range(len(B)):
    print(''.join(answer[r]))
"""

#숙제 6. 프로그래머스 다트 게임
"""
def solution(dartResult):
    answer = [0,0,0,0]
    i = 0
    j = 1
    Bonus = {'S':1, 'D':2, 'T':3}
    while i < len(dartResult):
        if dartResult[i:i+2] == '10':
            answer[j] = 10
            i += 2
        elif '0' <= dartResult[i] <= '9':
            answer[j] = int(dartResult[i])
            i += 1
        elif dartResult[i] == 'S' or dartResult[i] == 'D' or dartResult[i] == 'T':
            answer[j] = answer[j] ** Bonus[dartResult[i]]
            i += 1
            j += 1
        elif dartResult[i] == '*':
            answer[j - 1] = answer[j -1]*2
            answer[j - 2] = answer[j -2]*2
            i += 1
        elif dartResult[i] == '#':
            answer[j - 1] *= -1
            i += 1

    return sum(answer)
"""

def solution(dartResult):
    answer = 0
    Bonus = ['S', 'D', 'T']
    Option = ['*', '#']

    Out = [[]]
    cur_dart_score = []
    last_dart_score = []
    for i in range(len(dartResult)):
        if dartResult[i] in Bonus or dartResult[i] in Option:
            if dartResult[i] == 'S':
                cur_dart_score.append('**1')
            elif dartResult[i] == 'D':
                cur_dart_score.append('**2')
            elif dartResult[i] == 'T':
                cur_dart_score.append('**3')
            elif dartResult[i] == '*':
                cur_dart_score.append('*2')
                last_dart_score.append('*2')
            elif dartResult[i] == '#':
                cur_dart_score.append('*-1')
        else:
            if cur_dart_score[len(cur_dart_score)-1] == '1' and dartResult[i] == '0':
                pass
            cur_dart_score.append(dartResult[i])

    for scores in Out:
        answer += eval(''.join(scores))

    return answer

print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))
