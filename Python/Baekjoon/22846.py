import sys
input = sys.stdin.readline

A, B, C, M = map(int, input().rstrip().split())
# A = 한시간에 사용하는 피로도,  B = 한시간에 처리할 수 있는 일, C = 한시간을 쉬면 회복되는 피로도, M = 번아웃 임계 피로도
p = 0
w = 0

for _ in range(24):
    if p + A <= M:
        p = p + A
        w += B
    else:
        if p - C >= 0:
            p = p - C
        else:
            p = 0
print(w)