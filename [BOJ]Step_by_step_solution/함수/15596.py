def solve(a: list) -> int:
    answer = 0
    for i in range(len(a)):
        answer += a[i]
    return answer

solve([1, 2, 4, 5])