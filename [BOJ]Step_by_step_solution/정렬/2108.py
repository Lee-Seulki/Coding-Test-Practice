from collections import Counter
import sys

N = int(sys.stdin.readline())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))

nums.sort()
print(round(sum(nums)/N))
print(nums[N//2])

# 최빈값 중 두 번째로 작은 값을 출력한다.
nums_mode = Counter(nums).most_common()
if len(nums_mode) > 1:
    if nums_mode[0][1] == nums_mode[1][1]:
        print(nums_mode[1][0])
    else:
        print(nums_mode[0][0])
else:
    print(nums_mode[0][0])

print(max(nums)-min(nums))
# print(nums[-1] - nums[0])