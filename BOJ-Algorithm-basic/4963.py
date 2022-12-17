# 섬의 개수
import sys
sys.setrecursionlimit(10**4)
'''
한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 
걸어갈 수 있는 사각형이다. 
'''
def dfs(x, y):
    # 범위를 벗어나는 경우 즉시 종료
    if x < 0 or x >= h or y < 0 or y >= w:
        return False
    
    # 섬(1)인 경우
    if graph[x][y] == 1:
        graph[x][y] = 0

        dfs(x-1, y)
        dfs(x-1, y-1)
        dfs(x, y-1)
        dfs(x+1, y-1)
        dfs(x+1, y)
        dfs(x+1, y+1)
        dfs(x, y+1)
        dfs(x-1, y+1)
        return True
    return False

while True:
    w, h = map(int, input().split()) # 가로, 세로
    if w == 0 or h == 0:
        break
    else:
        graph = []
        for _ in range(h):
            graph.append(list(map(int, input().split())))

        cnt = 0
        for i in range(h):
            for j in range(w):
                if dfs(i, j) ==  True:
                    cnt += 1
        print(cnt)