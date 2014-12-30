# Modified version of bubble sort; once it recognizes the list is sorted, it will stop the operation.

def shortbubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    for passnum in range(len(alist)-1,0,-1):
        exchange = False
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                exchange = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum - 1

alist = [54,26,93,17,77,31,44,55,20]
shortbubbleSort(alist)
print(alist)