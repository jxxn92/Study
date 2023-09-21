import sys
input = sys.stdin.readline

N = int(input())
num_list = [0] * N
postfix = str(input().rstrip())
stack = []

for _ in range(N):
    num_list[_] = int(input())

print(num_list)

for i in postfix:
    if 'A' <= i and i <= 'Z':
        stack.append(num_list[ord(i)-ord('A')])
    else:
        pop2 = stack.pop()
        pop1 = stack.pop()

        if i == '*':
            stack.append(pop1*pop2)
        if i == '/':
            stack.append(pop1/pop2)
        if i == '+':
            stack.append(pop1+pop2)
        if i == '-':
            stack.append(pop1-pop2)

print('%.2f' %stack[0])	