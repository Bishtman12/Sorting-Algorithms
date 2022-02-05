def Insertion_Sort_Iterative(alist):
	n = len(alist)
	for index in range(n):
		j = index - 1
		while j>=0:
			if alist[index] < alist[j]:
				alist[index], alist[j] = alist[j], alist[index]
				index = j
				j = j - 1
			else:
				break
	return alist
A = [5,2,16,7,1,0]
print(Insertion_Sort_Iterative(A))
