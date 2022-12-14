FOUR_DIR = [
    # 위
    [-1, 0],
    # 아래
    [1, 0],
    # 왼쪽
    [0, -1],
    # 오른쪽
    [0, 1]
]

def solution(N, M, icemap):
    '''
    만들 수 있는 아이스크림 개수 확인
    '''
    answer = 0
    # start_pos = []
    # for i, row in enumerate(icemap):
    #     for j, v in range(row):
    #         # 얼음을 만들 수 있으면
    #         if v == 0:
    #             # 시작할 수 있는 포지션에 넣어줌
    #             start_pos.append((i, j))

    start_pos = [(i, j) for i, row in enumerate(icemap) for j, v in range(row) if v == 0]

    # used_map = []
    # for i in range(N):
    #     temp = []
    #     for j in range(M):
    #         temp.append(0) # 아직 안만들었으면 0
    #     used_map.append(temp)
    
    used_map = [[0]*M for _ in range(N)]
    # 시작할 수 있는 위치를 반복문을 통해 하나씩 가져온다
    for pos in start_pos:
        i, j = pos
        # 만약 해당 위치가 이미 사용했다면 시작할 수 없으니 다음으로 넘어간다(skip)
        if used_map[i][j] == 1:
            continue
        # 스택 생성
        q = [(i, j)]
        while q:
            now_i, now_j = q.pop()
            # 상, 하, 좌, 우 체크하기
            for i_dir, j_dir in FOUR_DIR:
                next_i = now_i + i_dir
                next_j = now_j + j_dir
                # 큰 맵을 벗어나는 지 확인(정상적인 맵 안에서 활동을 하도록 조건문 걸어주기)
                if 0 <= next_i <= N and 0 <= next_j <= M:
                    if icemap[next_i][next_j] == 0 and used_map[next_i][next_j] == 0:
                        # 사용 체크
                        used_map[next_i][next_j] = 1
                        q.append((next_i, next_j))
        answer += 1
    return answer

# print(solution(N, M, icemap))