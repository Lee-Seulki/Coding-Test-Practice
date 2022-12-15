import sys
input = sys.stdin.readline

n = int(input())
triangle = []

for _ in range(n):
    triangle.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(triangle[i])):
        if j == 0:
            upper_left_value = 0
        else:
            upper_left_value = triangle[i-1][j-1]
        
        if j == i:
            upper_right_value = 0
        else:
            upper_right_value = triangle[i-1][j]
        
        triangle[i][j] = triangle[i][j] + max(upper_left_value, upper_right_value)

print(max(triangle[-1]))