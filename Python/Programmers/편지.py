array = [2, 1, 4]
array = [9, 10, 11, 8]
answer = []

array2 = sorted(array)

max_array = array2[-1]

answer.append(max_array)
answer.append(array.index(max_array))

print(answer)