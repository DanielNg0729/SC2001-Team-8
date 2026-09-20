'''
SC2001 Lab Project 1: Integration of Merge Sort & Insertion Sort

'''
import random

def insertion_sort(arr, low = None, high = None):
    # Sort arr[low:high]
    if low == None:
        low = 0
    if high == None:
        high = len(arr) - 1
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

def merge_sort(arr, low = None, high = None):
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


def hybrid_sort(arr, s, low, high):
    # s here is the threshold
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1
    # length is the length of the part we do the sorting
    length = high - low + 1
    if length <= s:
        return insertion_sort(arr, low, high)
    mid = (low + high) // 2
    c = hybrid_sort(arr,s,low,high)
    c += hybrid_sort(arr,s,mid + 1,high)
    c += merge(arr, low, mid, high)
    return c


def generate_data(n, x ,seed = 1):
    rng = random.Random(seed) # Added seed to control the variant, remove seed for random
    return [rng.randint(1, x) for _ in range(n)]

print(generate_data(10,10))
