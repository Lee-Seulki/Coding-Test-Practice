import sys
input = sys.stdin.readline

# 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬
N = int(input())
members = []

for _ in range(N):
    age, name = input().split()
    members.append([int(age), name])

# 나이만 비교해서 정렬
members.sort(key = lambda x : x[0])

for member in members:
    print(member[0], member[1])
