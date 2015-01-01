# This function uses the binary method to find a number in a list.
# If not found, returns None. If found, returns the number with the index of the item in the list.

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first <=last and not found:
        midpoint = (first + last)/2
        if alist[midpoint] == item:
            found = True
            itemindex = alist.index(item)
            return found, itemindex
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))