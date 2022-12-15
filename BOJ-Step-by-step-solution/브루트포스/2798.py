from itertools import permutations

N, M = map(int, input().split())
card_nums = list(map(int, input().split()))

# N장의 카드 중 3장의 카드를 골라야 한다.
# 합이 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다
permutations_card = permutations(card_nums, 3)

answer = 0
for c in permutations_card:
    if M >= sum(c):
        answer = max(answer, sum(c))
print(answer)
