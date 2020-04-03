arr = [15,6,7,5,4,19,20]
n = len(arr)

'''Implementing all sorting algorithms in Python
   Bubble Selection Insertion Merge(*) 	
'''

def Bubble(arr):
	
	for i in range(n):
		for j in range(0,n-1-i):
			if arr[j]>arr[j+1]:
				arr[j+1], arr[j] = arr[j], arr[j+1]

	for i in range(n):		
		print(arr[i])

def Selection(arr):
	
	for i in range(n):
		min_index = i
		for j in range(i+1,n):
			if arr[j]<arr[min_index]:
				min_index = j
		arr[i],arr[min_index]=arr[min_index],arr[i]

def Insertion(arr):

	for i in range(1,n):
		key = arr[i]
		j=i-1
		
		while j >= 0 and key < arr[j]:
			arr[j + 1] = arr[j] 
			j -= 1
        arr[j + 1] = key 

# def Merge(arr):
# 	if n >1:
# 		mid = n//2
# 		L = arr[:mid]
# 		R = arr[mid:]		

# 		Merge(L)
# 		Merge(R)

# 		i = j = k =0
# 		while i < len(L) and j < len(R):
# 			if L[i] < R[j]:
# 				arr[k] = L[i]
# 				i+=1
# 			else:
# 				arr[k] = R[j]
# 				j+=1
# 			k+=1

# 			while i<len(L):
# 				arr[k]=L[i]
# 				i+=1
# 				k+=1

# 			while j< len(R):
# 				arr[k]=R[j]

#def 

# Selection(arr)
# Bubble(arr)
# Insertion(arr)
# Merge(arr)
for i in range(len(arr)):
	print(arr[i])