# baekjoon 1919 애너그램 만들기
lst = [0] * 26
s = 0
for i in list(input()):
    lst[ord(i) - 97] += 1
for j in list(input()):
    lst[ord(j) - 97] -= 1
for i in range(len(lst)):
    s += abs(lst[i])

print(s)