import sys
# input = sys.stdin.readline()
N = int(input())
numlist = []
for _ in range(N):
    numlist.append(int(sys.stdin.readline()))

numlist.sort()

print('\n'.join(map(str, numlist)))