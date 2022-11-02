N = int(input())
hansu = 0

for n in range(1, N+1):
    if n <= 99:
        hansu += 1
    else:
        n = str(n)
        if int(n[0])-int(n[1]) == int(n[1])-int(n[2]):
            hansu += 1

print(hansu)