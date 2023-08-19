n = 1
cnt = 0
if n == 1:
    print(-1)
else:
    while n != 1:
        if n % 2 == 0:
            n = n/2
            cnt += 1
        elif n % 2 != 0:
            n = n * 3 + 1 
            cnt += 1

    if cnt <= 0 or cnt > 500:
        print(-1)
    else:
        print(cnt)