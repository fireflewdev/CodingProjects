import math
sum = 0
count = 0
final = 1000
while (count < final):
	count += 1
	if (count % 3 == 0):
		sum = sum+count
	elif (count % 5 == 0):
		sum = sum+count
print(sum)
