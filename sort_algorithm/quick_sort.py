import sys

arr11 = [1,5,2,9,11,-2,10,4,2,7,6,4,9,1,10]
arr12 = arr11[:]

def partition(array, left, right):
    signal = array[right]

    small = []
    large = []
#    print "len to sort:", len(array[left: right])
    for data in array[left: right]:
        if data > signal:
            large.append(data)
        else:
            small.append(data)
    array[left:right+1] = small + [signal] + large
    print "left:", left, "right:", right, "small:", small, "large:", large, "signal:", signal, "mid:", len(small) - 1, "all:", array
    return left + len(small) - 1
    
def quick_sort(array, left, right):
    if left >= right:
        return
    mid = partition(array, left, right)
#    print "left mid right:", left, mid, right
    if left < mid:
        quick_sort(array, left, mid)
    if mid + 1 < right:
        quick_sort(array, mid + 1, right)
    
def do_quick_sort(array):
    quick_sort(array, 0, len(array) - 1)
    print array
    
if "__main__" == __name__:
    do_quick_sort(arr12)
