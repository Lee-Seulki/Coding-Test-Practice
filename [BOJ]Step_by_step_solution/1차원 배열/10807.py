# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.
# 첫째 줄에 입력으로 주어진 N개의 정수 중에 v가 몇 개인지 출력한다.
N = int(input())
num_list = list(map(int, input().split()))
v = int(input())
print(num_list.count(v))