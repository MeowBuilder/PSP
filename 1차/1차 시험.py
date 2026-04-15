from collections import deque

# A. 극장 컵홀더
"""
N = int(input())
sheat = list(input())
answer = ['']
count = 0
for i in range(len(sheat)):
    if sheat[i] == 'S':
        if answer[count] != '*':
            answer.append('*')
            answer.append(sheat[i])
            count += 2
    elif sheat[i] == "L":
        if answer[count] == 'L':
            if answer[count-1] == 'L':
                answer.append('*')
                answer.append(sheat[i])
                count += 2
            else:
                answer.append(sheat[i])
                count += 1
        else:
            answer.append('*')
            answer.append(sheat[i])
            count += 2

        pass
answer.append('*')
sheat_count = answer.count('S') + answer.count('L')
print(min(answer.count('*'),sheat_count))
"""
# B. 스도쿠
"""
N = int(input())
board = []
for _ in range(N):
    sub_board = [input() for _ in range(13)]
    board.append(sub_board)
answer_board = []
for row in board:
    num_board = []
    for col in row:
        sub_board = []
        if col[0] == '+':
            continue
        for char in col:
            if char.isdigit():
                sub_board.append(int(char))
            elif char == '.':
                sub_board.append('.')
        num_board.append(sub_board)
    answer_board.append(num_board)

for board in answer_board:
    answer = 'Y'
    for row in board:
        if answer == 'N':
            break

        for i in range(1,10): #한줄 검사
            if row.count(i) > 1:
                answer = 'N'
                break

        for i in range(9):
            if answer == 'N':
                break
            sub_set = set()
            for j in range(9):
                if board[j][i] == '.':
                    continue
                a = len(sub_set)
                sub_set.add(board[j][i])
                if a == len(sub_set):
                    answer = 'N'
                    break

    for i in range(3):
        if answer == 'N':
            break
        for j in range(3):
            if answer == 'N':
                break
            sub_set = set()
            for r in range(3):
                if answer == 'N':
                    break
                for c in range(3):
                    if answer == 'N':
                        break
                    if board[(i*3)+r][(j*3)+c] == '.':
                        continue
                    a = len(sub_set)
                    sub_set.add(board[(i*3)+r][(j*3)+c])
                    if a == len(sub_set):
                        answer = 'N'
                        break
    print(answer)
"""
# C. Kod
n = int(input())

score_h = list(map(int,input().split()))
score_us = list(map(int,input().split()))

score_usd = list()
for i in range(n):
    score_usd.append((i,score_us[i]))
score_usd.sort(key = lambda x : x[1],reverse=True)

final_score = [0 for _ in range(n)]

for i in range(len(score_h)):
    final_score[score_h[i]-1] += n-i
for i in range(len(score_usd)):
    final_score[score_usd[i][0]] += n-i
rank = list()
for i in range(n):
    rank.append((i,final_score[i]))
rank.sort(key = lambda x : x[1],reverse=True)

for i in range(n):
    print(f"{i+1}. Kod{rank[i][0]+1:0>2} ({rank[i][1]})")

# D. 적록색약
# E. 스타트링크
# F. 손님 대접
"""from itertools import combinations
N,M = map(int,input().split())

foods = [[] for _ in range(N)]
for i in range(N):
    personal = list(map(int,input().split()))
    for j in range(M):
        foods[j].append(personal[j])

for i in range(M):
 for food_comb in combinations(foods,i)
"""