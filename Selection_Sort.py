# This algos finds the min element then insert it at that exact position

def find_min_index(A,l,r):

    min_index = l
    for i in range(l,r):
        if A[min_index]> A[i]:
            min_index = i
    return min_index
def swap(A,index1,index2):
    A[index1] , A[index2] = A[index2] , A[index1]

def SelectionSort(A):
    sorted = 0
    for i in range(len(A)):
        min_index = find_min_index(A,sorted,len(A))
        swap(A,min_index,sorted)
        sorted += 1
    return A
A = [9,5,6,1,2,0]
print(SelectionSort(A))
