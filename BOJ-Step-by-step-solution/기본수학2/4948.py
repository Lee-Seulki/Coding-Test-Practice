# n보다 크고, 2n보다 작거나 같은 소수의 개수
def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

numlist = list(range(2, 246912))
memo = []

for i in numlist:
    if isPrime(i):
        memo.append(i)

while True:
    n = int(input())
    sosu = 0
    if n == 0:
        break
    for m in memo:
        if n < m <= 2*n:
            sosu += 1
    print(sosu)
