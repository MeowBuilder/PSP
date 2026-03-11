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