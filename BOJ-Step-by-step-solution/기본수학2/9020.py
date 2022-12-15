# 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것
# 두 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 함
def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

T = int(input())
for _ in range(T):
    n = int(input())
    a, b = n//2, n//2
    while a > 0: 
        if isPrime(a) and isPrime(b):
            print(a, b)
            break
        a -= 1
        b += 1   