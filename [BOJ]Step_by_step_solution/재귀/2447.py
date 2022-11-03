def make_star(star):
    board = [] # 별을 그릴 보드
    for i in range(3*len(star)):
        if i // len(star) == 1: # 3의 배수인 부분 처리
            board.append(star[i%len(star)] + ' '*len(star) + star[i%len(star)])
        else:
            board.append(star[i%len(star)]*3)
    return board

star = ['***', '* *', '***']

N = int(input())
cnt = 0

while N > 3:
    N //= 3
    cnt += 1

for i in range(cnt):
    star = make_star(star)

for i in star:
    print(i)
