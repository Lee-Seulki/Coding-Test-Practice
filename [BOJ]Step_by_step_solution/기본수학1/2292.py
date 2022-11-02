N = int(input())
# 6의 배수만큼 커짐(한바퀴)
nums = 1 # 벌집의 개수
cnt = 1 # 시작과 끝 값 포함
while N > nums:
    nums += 6 * cnt
    cnt += 1

print(cnt)