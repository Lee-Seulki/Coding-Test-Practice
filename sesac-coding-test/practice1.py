with open('./practice1.txt', 'r') as f:
    money_list = map(int, [l.rstrip() for l in f.readlines()])

def solution1(N:int):
    answer = 0
    coins = [500, 100, 50, 10]
    # 1. 500원짜리 거슬러주기
    answer += N // 500 # => 몫 (개수)
    remains = N % 500 # => 나머지 (잔돈)

    # 2. 100원짜리 거슬러주기
    answer += remains // 100
    remains = remains % 100

    # 3. 50원짜리 거슬러주기
    answer += remains // 50
    remains = remains % 50

    # 4. 10원짜리 거슬러주기
    answer += remains // 10
    remains = remains % 10

    with open('./remains.txt', 'a') as f:
        f.write(str(remains)+'\n')
        
    return answer

def solution2(N:int):
    answer = 0
    coins = [500, 100, 50, 10]
    for coin in coins:
        answer += N // coin
        N %= coin
    return answer

answer_list = []
for m in money_list:
    answer_list.append(solution1(m))

with open('./answer1.txt', 'w') as f:
    f.write('\n'.join(map(str, answer_list)))