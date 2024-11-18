import random

def play_game():
    """Function to handle the guessing game loop."""
    computer_guess = random.randint(1, 10)
    attempts = 0
    
    while True:
        try:
            user_guess = int(input("Guess a number between 1 and 10: "))
            if 1 <= user_guess <= 10:
                attempts += 1
                if user_guess == computer_guess:
                    print(f"Nice! You've guessed it right in {attempts} attempts!")
                    break
                elif user_guess > computer_guess:
                    print("Too high! Try again.")
                else:
                    print("Too low! Try again.")
            else:
                print("Please guess a number within the range of 1 to 10.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    """Main function to handle game initialization and replay prompt."""
    while True:
        user_choice = input("Would you like to play the guessing game? Please answer with 'yes' or 'no': ").strip().lower()
        
        if user_choice == 'yes':
            print("Great! Let's start the game.")
            play_game()
            play_again = input("Do you want to play again? Please answer with 'yes' or 'no': ").strip().lower()
            
            if play_again == 'no':
                print("Thanks for playing! Have a nice day!")
                break
            elif play_again != 'yes':
                print("Invalid input. Exiting the game. See you soon!")
                break
                
        elif user_choice == 'no':
            print("Alright! Have a great day!")
            break
        else:
            print("Please respond with 'yes' or 'no'.")

# Run the game
if __name__ == "__main__":
    main()
