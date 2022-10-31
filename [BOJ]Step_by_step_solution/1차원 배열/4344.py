C = int(input())
for _ in range(C):
    scores = list(map(int, input().split()))
    avg = sum(scores[1:])/scores[0] # 평균
    stu = 0 # 평균이 넘는 학생 수
    for score in scores[1:]:
        if score > avg:
            stu += 1
    ratio = stu / scores[0] * 100
    print('%.3f%%'%(ratio))