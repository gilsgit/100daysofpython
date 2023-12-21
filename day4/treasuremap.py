line1 = [" ","️ ","️ ️"]
line2 = [" ️"," ️","️ ️"]
line3 = [" ️️"," ️️"," ️️"]
map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")
position = input("Enter the coordinate ex A3") # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")