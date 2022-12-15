N = int(input())
scores = list(map(int, input().split()))
# 점수/M*100
M = max(scores)
new_scores = []
for score in scores:
    new_scores.append(score /M*100)
print(sum(new_scores)/len(new_scores))