# 124나라의 숫자: https://school.programmers.co.kr/learn/courses/30/lessons/12899
def solution(n):
    answer = ''
    nums124 = ['4', '1', '2'] # 나머지가 0, 1, 2 
    # 기존 3진법에서 3만 4로 대체
    
    while n > 0:
        answer = nums124[n%3] + answer
        # 3의 배수인 경우 체크
        if n%3 == 0:
            n = n//3 -1
        else:
            n //= 3
        
    return answer