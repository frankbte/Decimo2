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

def merge_arrays(arr1, arr2):
    merged = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    merged.extend(arr1[i:])  
    merged.extend(arr2[j:]) 

    return merged

def mezcla(arr1, arr2):
    i, j, k = 0, 0, 0
    n1, n2 = len(arr1), len(arr2)
    auxiliar = []

    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            auxiliar.append(arr1[i])
            i += 1
        else:
            auxiliar.append(arr2[j])
            j += 1
        k += 1

    while i < n1:
        auxiliar.append(arr1[i])
        i += 1
        k += 1

    while j < n2:
        auxiliar.append(arr2[j])
        j += 1
        k += 1

    return auxiliar