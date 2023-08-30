tree = ["A", "B", "C", "D", "E", "F", None, "G"]

i = 0
n = len(tree)
while i < n:

    if tree[i]:
        print(f"Parent: {tree[i]}", end=', ')
        left = 2 * i + 1
        right = left + 1
        if left < n and tree[left] is not None:
            print(f"Left: {tree[left]}", end=', ')
        if right < n and tree[right] is not None:
            print(f"Right: {tree[right]}",end=', ')
        print()
    i += 1