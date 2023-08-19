arr = [4,2,3,1]

if len(arr) == 1:
    del arr[0]
    arr.append(-1)
else:
    m = min(arr)
    arr.remove(m)
print(arr)