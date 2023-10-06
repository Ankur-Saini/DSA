def printMin(l, min_so_far = 2 ** 16):
    if len(l) == 0:
        print(min_so_far)
        return
    new_min = min(min_so_far, l[0])
    printMin(l[1:], new_min)

printMin([1,2,3,4,0,5,-2,4,-2,-4,6,7,8,3])