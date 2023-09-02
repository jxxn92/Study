import sys
input = sys.stdin.readline

n = int(input()) # 받을 문자열의 개수

for _ in range(n):
    a = list(map(str,input().split()))
    a[0] = sorted(a[0])
    a[1] = sorted(a[1])
    
    if (a[0] == a[1]):
        print("Possible")
    else:
        print("Impossible")