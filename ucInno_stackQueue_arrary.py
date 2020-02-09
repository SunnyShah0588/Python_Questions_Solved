class stackQueue:

	def __init__(self, n):

		self.size =  n
		self.arr = [None]*n
		self.top1 = -1
		self.top2 = self.size 
		self.s1 = [None] * n
		#self.s2 = [None]

	def push(self, x):

		if self.top1 < self.top2 - 1:
			self.top1 = self.top1 + 1
			self.arr[self.top1] = x

		else:
			print("Stack Overflow")
			exit(1)

	def pop(self):

		if self.top1 >= 0:
			x = self.arr[self.top1]
			self.arr[self.top1] = None
			self.top1 = self.top1 - 1

			return x

		else:
			print("Stack Empty")
			exit(1)

	def enqueue(self, x):

		while len(self.arr) != 0:

			self.s1.append(self.arr[-1])
			self.arr.pop()

		self.arr.append(x)

		while len(self.s1) != 0:
			self.arr.append(self.s1[-1])
			self.s1.pop()

	def dequeue(self):

		if len(self.arr) == 0:
			print ("Queue is Empty")

		x = self.arr[0]
		self.top1 = self.top1-1
		self.arr[0] = None


		return (x)

if __name__ == '__main__':

	array = stackQueue(5)


	array.push(1)
	array.push(2)
	array.push(3)
	array.push(4)
	array.push(6)

	print(array.arr)

	print (array.pop())



	print (array.dequeue())

	print(array.arr)

	