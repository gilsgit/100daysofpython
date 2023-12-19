#names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random


names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

length = len(names)

number = random.randint(0 , (length - 1))

name = names[number]

print(f"{name} is going to buy the meal today!" )