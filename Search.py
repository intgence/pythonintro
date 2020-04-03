import math
class Search:
	def __init__(self,arr,x):
		self.arr = arr
		self.x = x


	def BinarySearch(self):
		first = 0
		last = len(self.arr)-1
		self.arr.sort()
		while first<=last:
			mid = int((first+last)/2)
			if self.arr[mid] == self.x:
				print('Element found!')
				break
			elif self.x>self.arr[mid]:
				first = mid+1
			else:
				last = mid-1
	
	def LinearSearch(self):
		s = 0
		for i in range(len(self.arr)):
			if self.arr[i] == self.x:
				print('Element Found!')
				s+=1

		if s==0:
			print('Element not present!')

	def JumpSearch(self):
		n = len(self.arr)
		step = math.sqrt(n)

		prev = 0
		while self.arr[int(min(step,n))] <self.x:
			prev = step
			step += math.sqrt(n)

			if prev >= n:
				print('Element not found!')
		
		while self.arr[int(prev)] <self.x:
			prev += 1

			if prev == min(step,n):
				print('Element not found!')
		
		if self.arr[int(prev)] == self.x:
			print('Element found!')
		
		


if __name__ == "__main__":
	s = Search([1,2,5,4,3,7],6)
	s.JumpSearch()
			
