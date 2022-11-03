import sys
input = sys.stdin.readline

def recursions(s, l, r):
    global cnt
    cnt += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursions(s, l+1, r-1)

def isPalindrome(s):
    return recursions(s, 0, len(s)-1)

for _ in range(int(input())):
    cnt = 0
    print(isPalindrome(input().rstrip()), cnt)