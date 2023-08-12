numbers = [1, 2, -3, 4, -5]
odd = []
even = []
for i in numbers:
    if i < 0:
        odd.append(i)
    elif i >= 0:
        even.append(i)
odd.sort()
even.sort()
print(odd, even)
if len(even)==1 and len(odd)==1:
    print(odd[0] * even[0])
elif len(odd) <= 1:
    print(even[-1]*even[-2])
elif len(even) <= 1:
    print(odd[0]*odd[1])
else:
    print(max((even[-1]*even[-2]),(odd[0]*odd[1])))

    
# if len(even) == 0:
#     print(max_odd)
# elif len(odd) == 0:
#     print(max_even)
# elif len(odd) == 1 and len(even):
#     print(odd[0] * even[0])
# else:
#     if max_odd > max_even:
#         print(max_odd)
#     else:
#         print(max_even)