import random
#random is module

random_integer = random.randint(1, 10)
print(random_integer)

#0.000 - 0.999
random_float = random.random()
print(random_float)

#between 0.00 - 4.9999
print(random_float * 5)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")