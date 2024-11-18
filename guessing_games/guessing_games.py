import random
user_choice = input("would you like to play the guessing games : please answer by yes or no : ").strip().lower()
if user_choice == 'yes' : 
    print("that's nice !")
    computer_guess = random_number = random.randint(1, 10)
    attempts = 0
    while True : 
        user_guess = int(input("print a number between 1 and 10 : "))
        if 1 <= user_guess <= 10:
            if user_guess == computer_guess :  
                print("Nice! you've got it in")
                print(f"You've got it in {attempts} attemps !")
                play_again = input("you want to play again? please answer by yes/no")
                if play_again == "yes" : 
                    break
                elif play_again == "no" :
                    print("Have a nice day, see you soon")
                else :
                    print("please answer by yes or no")
            elif computer_guess < user_guess :
                print("it's higher")
            else :
                print("it's lower")
            attempts += 1
        else :
            print("please guess a number within the given the range")
        

