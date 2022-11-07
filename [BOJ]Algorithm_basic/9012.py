T = int(input())

for _ in range(T):
    pstr = input()
    stack = []
    for i in pstr:
        if i == '(':
            stack.append(i)
        else: # i == ')' 일 경우
            if stack == []:
                stack = [False]
                # print('NO')
                break
            else:
                stack.pop()
        
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')