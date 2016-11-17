def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1, fillslot+1):
            # print() index locations 'not needed'
            print(fillslot)
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp

# test working: YES
# alist = [84,45,423,1,43,64,12,32,65,87,32]
# selectionSort(alist)
# print(alist)
