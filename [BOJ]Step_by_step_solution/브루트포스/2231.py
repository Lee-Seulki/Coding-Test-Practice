# 분해합
N = int(input())
# 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다

# 분해합 구하기
answer = 0
for i in range(1, N+1):
    lst = list(map(int, str(i)))
    s = i + sum(lst)
    if s == N:
        answer = i
        break
print(answer)