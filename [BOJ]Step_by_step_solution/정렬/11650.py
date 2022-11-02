N = int(input())
point = []
for _ in range(N):
    x, y = map(int, input().split())
    point.append([x, y])
point.sort()

for i in range(len(point)):
    for j in range(len(point[i])):
        print(point[i][j], end=' ')
    print()