import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n , money = map(int, input().split())
cnt = 0
arr = []

for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)

while money != 0:
    for i in arr:
        if money >= i:
            cnt += money // i
            money = money % i 
        else:
            continue
print(cnt)