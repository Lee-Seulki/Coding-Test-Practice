# 다섯 개의 자연수가 주어질 때 이들의 평균과 중앙값을 구하는 프로그램을 작성하시오.
import sys

num_list = []
for _ in range(5):
    num_list.append(int(sys.stdin.readline()))

num_list.sort()
num_avg = int(sum(num_list) / 5)
num_median = num_list[2]

print(num_avg)
print(num_median)