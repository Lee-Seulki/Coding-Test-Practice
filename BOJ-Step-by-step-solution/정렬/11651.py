N = int(input())
point = []
for _ in range(N):
    x, y = map(int, input().split())
    point.append([x, y])
point.sort(key=lambda x : (x[1], x[0]))

for p in point:
    print(p[0], p[1])