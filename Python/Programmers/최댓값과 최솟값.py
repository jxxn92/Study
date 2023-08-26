s = "-1 -2 -3 -4"
answer = []
s = list(s.split())
sorted(s)
ans = ''
lst = [int(i) for i in s]

answer.append(min(lst))
answer.append(max(lst))

ans += str(min(lst))
ans += ' '
ans += str(max(lst))
print(ans)