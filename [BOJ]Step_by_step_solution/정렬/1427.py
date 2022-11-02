# 각 자리수를 내림차순으로 정렬
N = list(input()) # 정렬하려고 하는 수 N
nums = []
for n in N:
    nums.append(int(n))
nums.sort(reverse=True)
for n in nums:
    print(n, end='')
