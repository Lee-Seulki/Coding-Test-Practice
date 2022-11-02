import math
# 소수 판별 알고리즘
def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

N = int(input())
nums = map(int, input().split())
cnt = 0 # 소수의 개수

for num in nums:
    if isPrime(num) == True:
        cnt += 1

print(cnt)