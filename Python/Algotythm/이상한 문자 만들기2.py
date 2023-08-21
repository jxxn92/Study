s = "  TRy HElLo  WORLD "
ans = ''
idx = 0
for i in range(len(s)):
    if s[i] == ' ':
        ans += s[i]
        idx = 0
    elif s[i].isalpha():
        if idx % 2 == 0:
            if s[i].islower():
                ans += s[i].upper()
                idx +=1
            else:
                ans += s[i]
                idx += 1
        elif idx % 2 != 0:
            if s[i].isupper():
                ans+=s[i].lower()
                idx += 1
            else:
                ans+=s[i]
                idx += 1

print(ans)