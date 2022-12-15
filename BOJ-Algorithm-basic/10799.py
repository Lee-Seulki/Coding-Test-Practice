import sys
input = sys.stdin.readline

s = list(input().rstrip())
stack = []
answer = 0

for i in range(len(s)):
    # 쇠파이프 1개가 새로 시작하거나 레이저인 경우
    if s[i] == '(':
        stack.append('(')
    
    # 쇠파이프 1개가 끝나거나 레이저인 경우
    else: # s[i] == ')' 인 경우
        if s[i-1] == '(': # ()이면 레이저임
            stack.pop()
            answer += len(stack) # 그전에 쌓인 ( 만큼 잘리는 거니까 answer에 +
        
        else: # 쇠파이프인 경우(쇠막대기의 끄트머리임)
            stack.pop()
            answer += 1 
    
print(answer)