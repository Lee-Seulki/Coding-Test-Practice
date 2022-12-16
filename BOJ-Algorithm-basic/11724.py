# 연결 요소의 개수
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        # print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
'''
이문제는 간단히 연결된 노드들을 간선을 따라 dfs 혹은 bfs로 돌면서 방문한 노드들은 방문기록을 남기면 된다. 
간선을 따라 연결된 노드들을 다 돌고 나서 dfs 나 bfs를 한번 빠져나올 때마다 카운트를 1씩 증가시켜서 총 몇번도는지만 체크하면 되는 문제이다.
'''
cnt = 0
for i in range(1, N + 1):
    if not visited[i]:  # 만약 방문하지 않았다면
        if not graph[i]:  # 만약 그래프가 비어있다면
            cnt += 1  # 개수 1개 추가
            visited[i] = True  # 방문 처리
        else:  # 만약 그래프가 비어있지 않다면(어느 점과 연결된 점이 있다면)
            bfs(graph, i, visited)  # 해당 i를 시작노드로 bfs를 돈다.
            cnt += 1  # 연결요소 를 +1개 해준다.

print(cnt)