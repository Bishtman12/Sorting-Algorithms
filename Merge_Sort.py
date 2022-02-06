def merge(arr, l, m, r):
    L = [0] * (m-l+1)
    R = [0] * (r-m)
    for i in range(len(L)):
        L[i] = arr[l + i]

    for j in range(len(R)):
        R[j] = arr[m+1 +j]
    i, j = 0,0
    k = l  # index of merged subarray
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)
    return arr

arr = [10 ,9 ,8 ,7 ,6 ,5 ,4, 3, 2, 1]
print(mergeSort(arr,0,len(arr)-1))
