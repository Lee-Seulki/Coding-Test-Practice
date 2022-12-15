N = int(input())
numlist = []
for _ in range(N):
    k = int(input())
    numlist.append(k)
numlist.sort()
for num in numlist:
    print(num)