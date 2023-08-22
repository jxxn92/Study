food = [1, 3, 4, 6]
lst = []
ans = ''
for i in range(1, len(food)):
    lst.append(food[i]//2)
for i in range(1, len(lst)+1):
    if lst[i-1] > 0:
        ans += (str(i)*int(lst[i-1]))
    elif lst[i-1] <= 0:
        continue
reverse = ans[::-1]
answer = ans+'0'+reverse
print(answer)