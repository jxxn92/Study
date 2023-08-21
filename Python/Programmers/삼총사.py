numbers = [-3, -2, -1, 0, 1, 2, 3]
numbers.sort()
answer = []
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        for k in range(j+1, len(numbers)):
            if (numbers[i] + numbers[j] + numbers[k] == 0):
                answer.append([numbers[i], numbers[j], numbers[k]])
print(len(answer))