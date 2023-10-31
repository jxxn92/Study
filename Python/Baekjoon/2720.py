import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    q = 0; d = 0; n = 0; p = 0
    m = int(input())
    if m >= 25:
        q += (m // 25)
        m = (m % 25)
    if m >= 10:
        d += (m // 10)
        m = (m % 10)
    if m >= 5:
        n += (m // 5)
        m = (m % 5)
    p = m
    print(q,d,n,p)

