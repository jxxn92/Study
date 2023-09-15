import sys
input = sys.stdin.readline

a = list(input().rstrip())
answer = ''

for i in a:
    if i >= 'A' and i <= 'Z':
        if ord(i)+13 > 90:
            answer += chr(ord(i)+13-26)
        else:
            answer += chr(ord(i) + 13)
    if i >= 'a' and i <= 'z':
        if ord(i) + 13 > 122:
            answer += chr(ord(i) + 13 - 26)
        else:
            answer += chr(ord(i) + 13)
    if not i.isalpha():
        answer += i
print(answer)