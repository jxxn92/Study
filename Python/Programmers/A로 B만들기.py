before = "allpe"
after = "apple"

# before = list(before)
after = list(after)

for i in range(len(after)):
    before = before.replace(after[i],"",1)
if len(before) == 0:
    print(1)
else:
    print(0)


'''
before = "elppa"
after = "apple" 

before = sorted(before)
after = sorted(after)

if before == after:
    print(1)
else:
    print(0)
'''