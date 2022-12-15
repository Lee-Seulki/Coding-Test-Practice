M = int(input())
N = int(input())

# M 이상 N 이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 합, 둘째 줄에 최솟값
# 소수가 없을 경우 첫째줄에 -1
import math
# 소수 판별 알고리즘
def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

sosu = []
for i in range(M, N+1):
    if isPrime(i) == True:
        sosu.append(i)

if sosu == []:
    print(-1)
else:
    print(sum(sosu))
    print(min(sosu))