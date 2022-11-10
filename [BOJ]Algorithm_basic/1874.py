import sys
input = sys.stdin.readline

# 내가 스택을 쌓다가 중간에 한번씩 pop을 한 데이터들을 나열한 순서도 동일해야함
n = int(input())
stack = []
answer = []
cur = 1
flag = 0

for i in range(n):
    num = int(input())
    while cur <= num: # 첫번째 수를 만날 때 까지 push 해줘야함
        stack.append(cur)
        answer.append('+')
        cur += 1
    
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        flag = 1
        break

if flag == 0:
    for i in answer:
        print(i)