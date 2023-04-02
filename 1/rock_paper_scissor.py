# import module random
import random

# Starting print statements
print("Rules for winning Rock paper scissor game as follows:\n")
print("1 - Rock vs paper->paper wins\n")
print("2 - Rock vs scissor->Rock wins \n")
print("3 - paper vs scissor->scissor wins \n")

# Number of Attempts
attempt_left = 3
#For storing score
user_score = 0
comp_score = 0

#User name
user = input("Enter your name : ")

while True:
    print("Attempt left %s \n"%attempt_left)

    print("Enter choice \n 1. Rock \n 2. Paper \n 3. Scissor \n")

    # to take the input from user
    choice = int(input("%s turn: "%user))

    # looping for user to enter corect input
    while choice > 3 or choice < 1:
        choice = int(input("enter valid input: "))


    # initialize value of choice_name variable
    # corresponding to the choice value
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissor'

    # print user choice
    print("user choice is: " + choice_name)
    print("\nNow its computer turn.......")

    # Comp choose number between 1,2,3 using random randint
    comp_choice = random.randint(1, 3)

    # looping for comp to choose its choice
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    #Give comp the variable on basis of its choice
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissor'

    print("Computer choice is: " + comp_choice_name)

    print(choice_name + " V/s " + comp_choice_name)

    # conditions for winning the game
    if((choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice ==1 )):
        print("Paper wins => ", end = "")
        result = "Paper"

    elif((choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1)):
        print("Rock wins =>", end = "")
        result = "Rock"
    else:
        print("scissor wins =>", end = "")
        result = "Scissor"

    # printing whether user or com wins
    if result == choice_name:
        print("<== %s WINS ==>\n"%user.upper())
        attempt_left = attempt_left - 1
        user_score = user_score + 1
    else:
        print("<== COMPUTER WINS ==>\n")
        attempt_left = attempt_left - 1
        comp_score = comp_score + 1


    # Attempt part
    if attempt_left==0:
        if user_score > comp_score:
            print("%s wins successfully with score %s"%(user,user_score))
            
        elif user_score < comp_score:
            print("Computer wins successfully with score %s"%comp_score)
            
    else:
        continue
    
    play_again = input("Play again? (y/n): ")
    print("\n")
    attempt_left = 3
    if play_again.lower() != "y":
        
        break
    
# To print after coming out of loop
print("\nThanks for playing")
