#for number in range(a, b): from a to but not the last digit b
#   print(number)

for number in range(1, 11):
    print(number)

for number in range(1, 11, 3):   #steps by 3
    print(number)

total = 0
for number in range(1, 101):
    total += number

print(total)