nums = [5, 9, 7, 1, 9]
target = 10

hashTable = {}

for i, num in enumerate(nums):
	print (i)
	print (num)
	print (nums)
	if target-num in hashTable:
		print (target-num)
		print ([nums[i], nums[hashTable[target-num]]])
		break
	hashTable [num] = i

