n = 8
if n % 2 == 0:
    n //= 2
    print('수박'*n)
elif n % 2 == 1:
    n //= 2
    print('수박'*n+"수")

# return str(('수박'*n)) if n % 2 == 0 else str(('수박'*n+"수"))