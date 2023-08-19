# s = "abcde12121212"
s = "qwer1212"

if len(s) % 2 == 0:
    idx = len(s)//2
    print(s[idx-1:idx+1])
else:
    idx = len(s)//2
    print(s[idx])