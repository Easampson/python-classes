def insertionSort(alist):
    for index in range(1,len(alist)):

        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue

# test working: YES
# alist = [42,34,65,1,32,542,23,13,654,234]
# insertionSort(alist)
# print(alist)
