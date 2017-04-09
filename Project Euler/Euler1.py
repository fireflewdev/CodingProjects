import math

sum = 0
count = 0
final = 1000

while (count < final):
    if (count % 3 == 0):
        sum += count
        count += 1
    elif (count % 5 == 0):
        sum += count
        count += 1
    else:
        print("error")

print(sum)
