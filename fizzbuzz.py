number = [12, 25, 15, 16, 99, 60, 22, 97]

for i, num in enumerate(number):
	if num % 3 == 0 and num % 5 == 0:
		print ('FizzBuzz')
	elif num % 3 == 0:
		print ('Fizz')
	elif num % 5 == 0:
		print ('Buzz')
	else:
		print (number[i])