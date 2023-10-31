import copy

lst = input().rstrip().split()
lst2 = [] 
lst3 = []

# if lst[0] == "D":
#     lst2.append("Tx")
#     for i in range(1, len(lst)):
#         if lst[i] == "7E" or lst[i] == "1B":
#             lst2.append("1B")
#             lst2.append(lst[i])
#         else:
#             lst2.append(lst[i])
if lst[0] == "Rx":
    lst2.append("D")
    for i in range(1,len(lst)):
        lst2.append(lst[i])
        if (lst[i-1] == "1B" and lst[i] == "7E"):
            lst2.pop(-2)
    print(lst2)
# D 7E 7C BA 78 1B 1B 1B 1B B6 7E 

# print(" ".join(lst2))


