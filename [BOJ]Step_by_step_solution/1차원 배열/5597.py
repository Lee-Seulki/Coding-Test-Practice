# 제출 안 한 학생 2명의 출석 번호를 구하시오
import sys
student = []
for _ in range(28):
    student.append(int(sys.stdin.readline()))

for num in range(1, 31):
    if num not in student:
        print(num)