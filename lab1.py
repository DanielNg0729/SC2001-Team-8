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
        
def merge_sort(arr):
    pass

# Merge function to support merge sort and hybrid sort
def merge(arr):
    pass

def hybrid_sort(arr):
    pass

