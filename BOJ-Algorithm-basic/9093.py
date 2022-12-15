T = int(input())

sen = []
for _ in range(T):
    sen.append(input().split())

for i in range(len(sen)):
    for j in range(len(sen[i])):
        print(sen[i][j][::-1], end=' ')
    print()