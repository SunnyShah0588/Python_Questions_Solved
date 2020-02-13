from memory_profiler import profile

#@profile (precision = 4)

arry1 = [13, 27, 35, 40, 49, 55, 59]
arry2 = [17, 35, 39, 40, 55, 58, 60]
counter = 0

arry3 = arry1 + arry2
arry3 = sorted(arry3)

for i in range (len(arry3)-1):
	if arry3[i] == arry3[i+1]:
		counter += 1

print(counter) 

