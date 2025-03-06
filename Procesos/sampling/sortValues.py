def BLOCK_LOW(id, p, n):
    return id * n // p

def BLOCK_HIGH(id, p, n):
    return (id + 1) * n // p - 1

def BLOCK_SIZE(id, p, n):
    return BLOCK_HIGH(id, p, n) - BLOCK_LOW(id, p, n) + 1

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
