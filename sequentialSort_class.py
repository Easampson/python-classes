def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else: 
            pos = pos+1

    return found


# test working: YES 
# alist = [1,43,23,54,23,65,87,2,364,5]
# print(sequentialSearch(alist, 43))
# print(sequentialSearch(alist, 5))
