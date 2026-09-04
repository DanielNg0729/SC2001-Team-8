'''
SC2001 Lab Project 1: Integration of Merge Sort & Insertion Sort

'''

def insertion_sort(arr, low, high):
    # Sort arr[low:high]
    count = 0
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low:
            count += 1 
            if arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    return count, arr
        

# Merge function to support merge sort and hybrid sort
def merge(arr, low, mid,high):
    left, right = arr[low: mid + 1], arr[mid + 1: high]
    count = 0
    i,j = 0,0
    k = low
    nl, nr = len(left), len(right)
    while i < nl and j < nr:
        count += 1
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < nl:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < nr:
        arr[k] = right[j]
        j += 1
        k += 1
    return count, arr

def merge_sort(arr, low, high):
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1
    if high <= low:
        return 0
    mid = (low + high) // 2
    c = merge_sort(arr,low,high)
    c += merge_sort(arr,mid+1,high)
    c += merge(arr, low, mid, high)
    return c


def hybrid_sort(arr):
    pass

