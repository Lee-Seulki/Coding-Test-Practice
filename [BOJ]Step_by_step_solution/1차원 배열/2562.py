ans = []
for i in range(9):
    num = int(input())
    ans.append(num)
    if ans[i] == max(ans):
        max_num = i+1
print(max(ans), max_num, sep='\n')