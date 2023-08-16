n = int(input())
answer = []
lst = list(map(int, input().split()))

for _ in range(len(lst)):
    answer.append(lst.pop())

print(*answer)