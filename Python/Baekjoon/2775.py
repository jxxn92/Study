import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    floor = int(input())
    room = int(input())

    lst = [j for j in range(1, room + 1)]
    
    for k in range(1, floor + 1):
        for l in range(1, room):
            lst[l] += lst[l-1]
    print(lst[-1])