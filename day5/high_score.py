# Input a list of student scores
student_scores = input("Enter a range of grades:\n").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇

high_score = 0
for number in student_scores:
  if number > high_score:
    high_score = number

print(f"The highest score in the class is: {high_score}")

