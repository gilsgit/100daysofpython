# round numbers  can add in decimal places to round to
print(round(8 / 3, 2))

# floor chops off numbers after decimal
print(8 // 3)

# F-STRINGS mix data types - put f infront of string
score = 0
height = 1.8
isWinning = True

print(f"your score is {score}, your height is {height}, your are winning is {isWinning}")

print("How old are you?")
age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

years_left = (90 - int(age))

weeks_left = (years_left * 52)

print(f"You have {weeks_left} weeks left.")