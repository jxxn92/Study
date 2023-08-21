s = "try hello world"
ans = ''
a = s.split()

for i in range(len(a)):
    for j in range(len(a[i])):
        if j % 2 == 0:
            if a[i][j].isupper():
                ans += a[i][j]
            else:
                ans += a[i][j].upper()
        else:
            if a[i][j].isupper():
                ans += a[i][j].lower()
            else:
                ans += a[i][j]
    ans += ' '
print(ans)
