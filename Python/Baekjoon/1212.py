import sys
input = sys.stdin.readline

n = str(input())
oc = '0o'
num = oc+n

ten = int(num, 8)

answer = format(ten, 'b')
print(answer)

