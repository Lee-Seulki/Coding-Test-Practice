# 로또의 최고순위와 최저순위: https://school.programmers.co.kr/learn/courses/30/lessons/77484?language=python3
def solution(lottos, win_nums):
    answer = []
    # 로또 순위를 결정하는 방식
    # 맞춘 개수: 순위
    score = {
        '6': 1,
        '5': 2,
        '4': 3,
        '3': 4,
        '2': 5,
        '1': 6,
        '0': 6
    }
    max_num = 0 
    min_num = 0 
    
    # 최고 순위
    for lotto in lottos:
        if lotto in win_nums:
            max_num += 1
        elif lotto == 0:
            max_num += 1
    answer.append(score[str(max_num)])
    
    # 최저 순위
    for lotto in lottos:
        if lotto in win_nums:
            min_num += 1
        elif lotto == 0:
            continue
    answer.append(score[str(min_num)])
        
    return answer