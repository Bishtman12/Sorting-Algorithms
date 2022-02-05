def swap(A,index1,index2):
    A[index1],A[index2] = A[index2], A[index1]
# swaps the adjacent elements if they're not in order. 
# 0(n^2) Worst Case and 0(1) space complexity
def bubbleSort_RECURSION(A):
    front = 1
    back = 0
    swaps = False
    while front < len(A):
        if A[front] < A[back]:
            swap(A,front,back)
            front += 1
            back += 1
            swaps = True
        else:
            front += 1
            back += 1
    if swaps is True:
        return bubbleSort_RECURSION(A)
    else:
        return A
def bubbleSort_Iteration(A):
    n = len(A)
    for i in range(n): # in the worst we will be making n iterations ( when minimum element is at the last index)
        swaps = False
        front = 1
        back = 0
        swaps = False
        while front < len(A):
            if A[front] < A[back]:
                swap(A, front, back)
                front += 1
                back += 1
                swaps = True
            else:
                front += 1
                back += 1
        if swaps == False:
            break
    return A

A = [5 ,1 ,4 ,2 ,8]
print(bubbleSort_RECURSION(A))
print(bubbleSort_Iteration(A))
