import math
sum = 0
count = 0
final = 1000

while (count < final):
    if (count % 3 == 0):
        print(count)
        sum += count
    elif (count % 5 == 0):
        print(count)
        sum += count
    count += 1
print(count)
print(sum)