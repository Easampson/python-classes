def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

# test woring: YES
# alist = [54,23,654,94,23,66,74,31,1]
# bubbleSort(alist)
# print(alist)

