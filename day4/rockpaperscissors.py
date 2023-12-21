import random

choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user_choice = int(choice)
computer = random.randint(0,2)
print(f"Computer chose {computer}")


if user_choice == computer:
    print("It's a draw!")
elif user_choice == 0 and computer == 1:
    print("computer wins")
elif user_choice == 0 and computer == 2:
    print("You win!")
elif user_choice == 1 and computer == 0:
    print("You win!")
elif user_choice == 1 and computer == 2:
    print("Computer wins!")
elif user_choice == 2 and computer == 0:
    print("Computer wins!")
else:
    print("You win!")




 



