# A를 오름차순 정렬한다
def merge_sort(A, p, r): # A=[]
    if (p < r and cnt <=K):
        q = (p+r)//2 # q는 p, r의 중간 지점
        merge_sort(A, p, q) # 전반부 정렬
        merge_sort(A, q+1, r) # 후반부 정렬
        merge(A, p, q, r) # 병합

# A[전반부]와 A[후반부]를 병합하여 오름차순 정렬된 상태로 만든다
def merge(A, p, q, r):
    global cnt, result

    i = p
    j = q+1
    tmp = []

    while (i<=q and j<=r):
        if (A[i] <= A[j]):
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
    
    while (i <= q): # 왼쪽 배열 부분이 남은 경우
        tmp.append(A[i])
        i += 1
    while (j <= r): # 오른쪽 배열 부분이 남은 경우
        tmp.append(A[j])
        j += 1

    i = p
    t = 0

    while (i <= r): # 결과를 A에 저장 
        A[i] = tmp[t]
        cnt += 1
        if (cnt == K):
            result = A[i]
            break
        i += 1
        t += 1

N, K = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
result = -1 # 저장 횟수가 K보다 작으면 -1 출력
merge_sort(A, 0, N-1)
print(result)