# a층의 b호에 살려면, 자신의 아래 (a-1)층의 1호부터 b호까지 사람들의 수 합만큼 사람들을 데려와 살아야 한다.
T = int(input())
# k층의 n호에는 몇명이 살고있는가
# 2층 10호에 살려면 1층의 1호부터 10호까지 사람들의 수의 합
# 0층의 n호에는 n명이 산다.
# 1층 n호에 살려면 0층의 1호부터 n호까지 사람들의 수의 합
for _ in range(T):
    k = int(input()) # 층
    n = int(input()) # 호
    k0 = [x for x in range(1, n+1)] # 0층 n호에 사는 사람수 배열
    for i in range(k):
        for j in range(1, n):
            k0[j] += k0[j-1]
    print(k0[-1])
            