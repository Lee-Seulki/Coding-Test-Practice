# n*A - n*B >= V
import sys
input = sys.stdin.readline
import math

A, B, V = map(int, input().split())
day = (V-B) / (A-B)
print(math.ceil(day))