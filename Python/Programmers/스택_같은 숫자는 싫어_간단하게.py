arr = [1, 3, 3, 0, 1, 1]

answer = []
answer.append(arr[0])

for x in range(1, len(arr)):
    if arr[x] != arr[x-1]:
        answer.append(arr[x])

print(answer)