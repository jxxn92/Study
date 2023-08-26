s = "xyzav"
skip = "wbqd"
index = 5
lst = []

for char in s:
    for i in range(1, index+1):
        if (ord(char)+i) > ord('z'):
            lst.append(chr(ord(char)+i-26))
        else:
            lst.append(chr(ord(char)+i))
    for j in lst:
        if j in skip:
            lst.remove(j)
    print(lst)
    if len(lst) != 5:
        ord(lst[-1])+1
    lst.clear()
