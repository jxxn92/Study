import sys
input = sys.stdin.readline

cnt = 0
for _ in range(int(input())):
    stack = [] # 스택
    string = list(input().rstrip()) # 좋은 단어인지 판별 할 문장
    if len(string) % 2 == 1: # 어쨌든 좋은 문장은 짝을 맞춰야 하기 때문에 홀수 라면 처음부터 짝이 맞지 않아 답이 될 수 없다 그렇기 때문에 홀수는 일단 제외
        continue
    else:
        for s in string:
            if not stack: # 스택이 비어있다면 일단 한 글자를 스택에 삽입 
                stack.append(s)
                continue
            else: # 스택에 값이 있다면
                if stack[-1] == s:
                    stack.pop()
                else:
                    stack.append(s)

    if len(stack) == 0:
        cnt += 1
    else:
        cnt += 0
print(cnt)