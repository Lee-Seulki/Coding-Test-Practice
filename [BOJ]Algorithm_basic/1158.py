from collections import deque
import sys
input = sys.stdin.readline

# 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 
N, K = map(int, input().split())
q = deque([i+1 for i in range(N)])
yose = []
while q:
    for _ in range(K-1):
        q.append(q.popleft()) # K번째 앞 까지의 요소들을 뒤로 보낸다
    yose.append(q.popleft()) # K번째를 popleft해서 yose에 append

print('<', end='')
for i in range(len(yose)-1):
    print(yose[i], end=', ')
print(str(yose[len(yose)-1])+'>')