lst = input().rstrip().split()
lst2 = [] 
lst3 = []

next_val = False

if lst[0] == "D":
    lst2.append("Tx")
    for i in range(1, len(lst)):
        if lst[i] == "7E" or lst[i] == "1B":
            lst2.append("1B")
            lst2.append(lst[i])
        else:
            lst2.append(lst[i])
if lst[0] == "Rx":
    lst2.append("D")
    for i in range(1,len(lst)):
        lst2.append(lst[i])
        if (lst[i-1] == "1B" and lst[i] == "7E"):
            lst2.pop(-2)
    for i in range(len(lst2)):
        if(next_val == True):
            next_val = False
            continue
        lst3.append(lst2[i])
        if(lst2[i] == "1B"):
            next_val = True
        
if(lst[0] == "D"):
    print(" ".join(lst2))
else:
    print(" ".join(lst3))


