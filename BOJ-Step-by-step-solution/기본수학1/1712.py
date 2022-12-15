A, B, C = map(int, input().split())
# C가 A+B보다 많아지게되는 지점을 손익분기점
# 총 수입 = 고정비용 + 가변비용
# C*N = A + B*N 
# 최초로 이익이 발생하는 판매량 출력
if B >= C:
    print(-1)
else:
    print(A//(C-B)+1)