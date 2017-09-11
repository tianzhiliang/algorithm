import sys

arr11 = [1,5,2,9,11,-2,10,4,2,7,6,4,9,1,10]
arr12 = arr11[:]

def merge_list(array, left, mid, right):
    i = left
    j = mid + 1
    buf = []
    while i <= mid and j <= right:
        if array[i] < array[j]:
            buf.append(array[i])
            i += 1
        else:
            buf.append(array[j])
            j += 1

    while i <= mid:
        buf.append(array[i])
        i += 1

    while j <= right:
        buf.append(array[j])
        j += 1

    array[left:right+1] = buf[:]
    print "left:", left, "mid:", mid, "right:", right, "leftdata:", array[left:mid+1], "rightdata:", array[mid+1: right+1], "res:", buf, "all:", array

def merge_sort(array, begin, end):
    mid = (begin + end) / 2

    if mid <= begin and mid >= end:
        return
    
    if mid > begin:
        #print "merge_sort l begin, mid, end:", begin, mid, end
        merge_sort(array, begin, mid)
    if mid < end:
        #print "merge_sort r begin, mid, end:", begin, mid, end
        merge_sort(array, mid + 1, end)
    merge_list(array, begin, mid, end)
    return

def do_merge_sort(array):
    merge_sort(array, 0, len(array) - 1)
    print array
 
    
if "__main__" == __name__:
    do_merge_sort(arr11)
