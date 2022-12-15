# DFS와 BFS
import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1) # dfs
visited2 = [0] * (N+1) # bfs

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문할 수 있는 정점이 여러개인 경우 정점 번호가 작은 것을 먼저 방문한다
for i in graph:
    i.sort()
# print(graph)

def dfs(graph, start, visited):
    # 현재 노드를 방문 처리
    visited[start] = True
    print(start, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True # 방문 처리
    
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

dfs(graph, V, visited)
print()
bfs(graph, V, visited2)