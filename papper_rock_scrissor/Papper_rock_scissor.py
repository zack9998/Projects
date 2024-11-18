import random
options = ['r','s','p']
while True : 
    pc_choice = random.choices(options)
    user_choice = input('please enter either rock "r" , papper "p" or scissor "s" : ')
    if user_choice in options : 
        if user_choice == pc_choice:
            print("it's a tie")
        elif ( (user_choice == 'r' and pc_choice== 's')
                or (user_choice == 'p' and pc_choice=='r')
                or (user_choice == 's' and pc_choice =='p') ):

                print("congratulation!! won")
        else : 
            print('you lost!')     
    else : 
        print("please enter a valid input : either s, p or r")
    while True :
        replay = input("do you want to replay ? please answer by yes or no : ")
        if replay == "yes" :
            print("great! let's play again ")
            break
        elif replay == 'no' :
            print("goodby !! see you soon")
            break
        else :
            print("please reply by 'yes' or 'no'")    
    if replay == 'no':
        break
