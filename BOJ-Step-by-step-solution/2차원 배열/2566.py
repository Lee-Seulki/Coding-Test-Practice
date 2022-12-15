import sys
input = sys.stdin.readline

A = []
for row in range(9):
    A.append(list(map(int, input().split())))

x = 0
y = 0
max = -1

for i in range(9):
    for j in range(9):
        if A[i][j] > max:
            max = A[i][j]
            x = i+1
            y = j+1

print(max)
print(x, y)