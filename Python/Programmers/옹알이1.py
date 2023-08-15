# babbling = ["aya", "yee", "u", "maa", "wyeoo"]	
babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]	
possible = ["aya", "ye", "woo", "ma"]
count = 0
for i in range(len(babbling)):
    for j in range(len(possible)):
        babbling[i] = babbling[i].replace(possible[j]," ")
        print(babbling)

for i in range(len(babbling)):
    babbling[i] = babbling[i].replace(' ','')
    
for i in range(len(babbling)):
    if len(babbling[i]) == 0:
        count += 1

print(count)