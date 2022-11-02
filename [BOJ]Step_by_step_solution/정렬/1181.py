import sys
input = sys.stdin.readline

# 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.
N = int(input())
words = []
for _ in range(N):
    words.append(input().strip())    
words = list(set(words))

words.sort()
words.sort(key = len)
for word in words:
    print(word)