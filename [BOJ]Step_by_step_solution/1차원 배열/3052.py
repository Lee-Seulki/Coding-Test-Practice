ans = []
for _ in range(10):
    num = int(input())
    ans.append(num%42)

ans = set(ans)
print(len(ans))