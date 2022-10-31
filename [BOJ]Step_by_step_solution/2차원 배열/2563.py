import sys
input = sys.stdin.readline

n = int(input())
# 가로, 세로의 크기가 각각 100인 정사각형 모양의 도화지
white_board = [[0]*100 for _ in range(100)]

for _ in range(n):
    a, b = map(int, input().split())

    # 가로 세로의 크기가 각각 10인 정사각형 모양의 색종이
    for i in range(b, b+10):
        for j in range(a, a+10):
            white_board[i][j] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if white_board[i][j]:
            cnt += 1
print(cnt)