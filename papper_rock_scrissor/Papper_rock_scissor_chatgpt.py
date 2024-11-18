import random

# Declare list of choices
options = ["r", "p", "s"]

# Ask user to choose their option
while True:
    user_choice = input('Choose either rock (r), paper (p), or scissors (s): ').lower()
    if user_choice not in options:
        print("Invalid choice. Please try again.")
        continue
    break

# Computer's choice
computer_choice = random.choice(options)
print(f"Computer choice is: {computer_choice}")

# Game rules
if computer_choice == user_choice:
    print("It's a tie!")
elif (computer_choice == "s" and user_choice == "p") or \
     (computer_choice == "r" and user_choice == "s") or \
     (computer_choice == "p" and user_choice == "r"):
    print("You lose!")
else:
    print("You win!")
