# 그리디 알고리즘이니까 5키로 설탕봉지 먼저 생각해주면 됨
N = int(input())
cnt = 0

while N >= 0:
    if N % 5 == 0:
        cnt += (N//5)
        print(cnt)
        break
    N -= 3
    cnt += 1
else:
    print(-1)