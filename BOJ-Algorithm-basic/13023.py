# ABCDE
# 위와 같은 친구 관계가 존재하는지 안하는지
# 해당 그래프의 깊이가 4 이상임을 증명
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
answer = False

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, start, visited, depth):
    global answer
    visited[start] = True
    
    # 깊이가 5면 True 반환
    if depth == 5:
        answer = True
        return
    
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited, depth+1)
    visited[start] = False

for i in range(N):
    dfs(graph, i, visited, 1)
    if answer:
        break

if answer:
    print(1)
else:
    print(0)