def solution(number, k):
    answer = ''
    # 문자열 내 요소를 숫자로 변환
    number = list(map(int, number))
    
    now_index = 0
    # 배열 길이 - k만큼 돌고 만약 남으면, 더이상 볼 필요 없음
    for i in range(len(number)-k):
        # 내가 볼 수 있는 부분만 (k+1만큼만 가져옴)
        remains = number[now_index : now_index+k+1]
        max_value = -1
        max_index = 0
        # 해당 부분 확인하면서 가장 큰 값, index 확인
        for j, v in enumerate(remains):
            # 만약 현재 값이 저장해둔 max_value보다 크면,
            if v > max_value:
                # 최신화
                max_value = v
                max_index = j
            # 단일자리에서 가장 큰 수는 9이기 때문에, 바로 break
            if max_value == 9: break
        
        # nox_index, k, answer 최신화
        # max_index는 remains의 index니까 (0부터 시작하기 때문에)
        # now_index + max_index 그 다음꺼부터 보기 위해 +1 해줌
        now_index += max_index + 1
        k -= max_index
        answer += str(max_value)
    
    return answer