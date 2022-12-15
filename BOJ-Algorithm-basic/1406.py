import sys
input = sys.stdin.readline

stack_l = list(input().strip())
stack_r = []

commands = []
for _ in range(int(input())):
    commands.append(input().split())

for command in commands:
    if command[0] == 'P':
        stack_l.append(command[1]) # 커서 왼쪽에 데이터 추가
    elif command[0] == 'L': 
        if stack_l: # 커서가 맨 앞이 아니라면
            stack_r.append(stack_l.pop()) 
    elif command[0] == 'D': 
        if stack_r: # 커서가 맨 오른쪽이 아닐 경우
            stack_l.append(stack_r.pop())
    elif command[0] == 'B':
        if stack_l:
            stack_l.pop()

stack_r.reverse()
print(''.join(stack_l+stack_r))
