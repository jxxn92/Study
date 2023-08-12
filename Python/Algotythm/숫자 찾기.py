def solution(num, k):
    lst = list(str(num))

    if str(k) in lst:
        return(lst.index(str(k))+1)
    else:
        return(-1)
            