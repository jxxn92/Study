import sys
input = sys.stdin.readline

s = str(input().rstrip())
answer = []

for i in range(len(s)):
    answer.append(s[i:])
answer.sort()

for i in answer:
    print(i)