print("Thank you for choosing Python Pizza Deliveries!")
print("Please enter the size of pizza: S, M or L")
size = input() # What size pizza do you want? S, M, or L
print("Do you want pepperoni? Y or N")
add_pepperoni = input() # Do you want pepperoni? Y or N
print("Do you want extra cheese? Y or N")
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
elif size == "L":
  bill =+ 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}")
