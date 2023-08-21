s = "a B z"	
n = 4
ans = ""
for i in s:
    if i == ' ':
        ans += i
    else:
        if i.isupper():
            if (ord(i) + n ) > 90:
                ans += (chr(ord(i)+n-26))
            else:
                ans += (chr(ord(i)+n))
        elif i.islower():
            if (ord(i) + n ) > 122:
                ans += (chr(ord(i)+n-26))
            else:
                ans += (chr(ord(i)+n))
print(ans)

# a ~ z = 97 ~ 122
# A ~ Z = 65 ~ 90 