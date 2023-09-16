def merge_sort(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2 # 절반으로 나누기 위해서 인덱스를 찾기 위해 mid 함수 호출
    
    low_arr = merge_sort(arr[:mid]) # [ 1, 3, 6, 9] # 반으로 나는 것 들중 하위 리스트를 다시 머지소트를 통해 정렬한다.
    high_arr = merge_sort(arr[mid:]) # [15, 2, 7, 8] # 반으로 나는 것 들중 상위 리스트를 다시 머지소트를 통해 정렬한다.

    merged_arr = [] # 병합할 리스트
    l = h = 0 # 병합 하면서 인덱스를 돌기 위해서 선언한 변수

    while l < len(low_arr) and h < len(high_arr): # low_arr 과 high_arr이 둘다 값이 있을때만 실행
        if low_arr[l] < high_arr[h]: # 높은 리스트의 값이 낮은 리스트에 값보다 크다면
            merged_arr.append(low_arr[l]) # 높은 리스트의 값을 병함 리스트에 append 시킨다
            l += 1 # 낮은 리스트에 있는 값 하나를 사용했으니 다음 인덱스 사용을 위해 +1 시킨다.
        else: # 낮은 리스트의 값이 높은 리스트의 값보다 크다면
            merged_arr.append(high_arr[h]) # 낮은 리스트의 값을 병합 인덱스에 append 시킨다.
            h += 1 # 낮은 리스트에 있는 값 하나를 사용했으니 다음 인덱스 사용을 위해 +1 시킨다
    merged_arr += low_arr[l:] # 이 문장을 실행 했다는 것은 일단 상위 리스트이던 하위 리스트이던 둘중에 하나의 리스트는 빈 값을 가진다는 뜻이므로
    merged_arr += high_arr[h:] # 두 리스트중 하나의 리스트는 값이 남아 있을 수도 있기 때문에 남은 값들을 병합 리스트에 추가 시키기 위해서 이 문장을 실행한다.

    return merged_arr # 병합된 리스트를 리턴해준다.

arr = [1, 3, 6, 9, 15, 2, 7, 21, 8]

print(merge_sort(arr))
