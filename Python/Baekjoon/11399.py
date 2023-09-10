import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().rstrip().split()))
a.sort()
sum1 = 0
sum2 = 0

for i in range(len(a)):
    sum1 += a[i]
    sum2 += sum1

print(sum2)