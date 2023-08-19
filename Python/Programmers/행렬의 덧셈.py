arr1 = [[1],[2]]
arr2 = [[3],[4]]    
ans = []
for a, b in zip(arr1, arr2):
    for i,j in zip(a,b):
        ans.append(i+j)
lst = [ans[i*len(arr1[0]):(i+1)*len(arr1[0])] for i in range(len(ans)//len(arr1[0]))]
print(lst)