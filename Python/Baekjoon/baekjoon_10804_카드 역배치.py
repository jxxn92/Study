card = list(range(1,21))


for i in range(10):
    first, last = map(int, input().split())
    card[first-1:last] = card[first-1:last][::-1]
print(*card)
    