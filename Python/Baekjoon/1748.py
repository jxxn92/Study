# 1 ~ 9 = 1글자
# 10 ~ 99 = 2글자
# 100 ~ 999 = 3글자
# 1000 ~ 9999 = 4글자
# 10000 ~ 99999 = 5글자
# 100000 ~ 999999 = 6글자
# 1000000 ~ 999999 = 7글자
import sys
input = sys.stdin.readline

n = str(input().rstrip())
l = len(n)

if l == 1:
    print(n * 1)
if l == 2:
    print((int(n)-9)*2 + 9)
if l == 3:
    print((int(n)-99)*3 + 189)
if l == 4:
    print((int(n)-999)*4 + 2889)
if l == 5:
    print((int(n)-9999)*5 + 38889)
if l == 6:
    print((int(n)-99999)*6 + 488889)
if l == 7:
    print((int(n)-999999)*7 + 5888889)
if l == 8:
    print((int(n)-9999999)*8 + 68888889)
if l == 9:
    print((int(n)-99999999)*9 + 788888889)





