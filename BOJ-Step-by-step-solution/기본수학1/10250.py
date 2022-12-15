# 정문으로부터 걷는 거리가 가장 짧도록 방을 배정하는 프로그램
T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    floor = N%H
    room_num = N//H+1
    if N%H == 0: # N이 H의 배수이면
        floor = H
        room_num = N//H
    room = floor*100 + room_num
    print(room)
