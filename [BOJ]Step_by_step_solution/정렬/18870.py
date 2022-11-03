# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.
# 좌표 압축: 흩뿌려진 좌표들을 연속된 수들로 모아 압축하는 것
# 작은 값 부터 시작해서 0부터 인덱스를 부여
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().rstrip().split()))

numset = list(set(nums))
numset.sort()

nums_dict = {}
for i in range(len(numset)):
    nums_dict[numset[i]] = i

for num in nums:
    print(nums_dict[num], end=' ')
