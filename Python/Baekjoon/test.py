n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(int(input()))

d = [10001] * (m+1)

print(arr)
print(d)