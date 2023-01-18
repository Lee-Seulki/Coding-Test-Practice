# 신고 결과 받기: https://school.programmers.co.kr/learn/courses/30/lessons/92334
def solution(id_list, report, k):
    answer = []

    info = {}
    # 동일한 유저에 대한 신고 횟수는 1회로 처리되므로 중복적용 x
    for user_id in id_list:
        info[user_id] = set()
    
    for r in report:
        # 신고한 사람, 신고를 당한 사람
        singo, singoed = r.split()
        # 신고당한 사람: 신고한 사람
        info[singoed].add(singo)

    mail = {}
    # 만약에 내가 신고한 유저가 k번 이상 신고를 받았으면, 메일을 받는다
    # mail을 받는 횟수를 +=1 해주는 부분
    for user_id in id_list:
        mail[user_id] = 0
    # 유저가 받는 메일 수를 계산
    for singoed in info:
        # k번 이상 신고를 당했으면
        if len(info[singoed]) >= k:
            # mail[ap, mu..] += 1
            for singo in info[singoed]:
                mail[singo] += 1
    
    print(mail)
    for cnt in mail.values():
        answer.append(cnt)
    return answer