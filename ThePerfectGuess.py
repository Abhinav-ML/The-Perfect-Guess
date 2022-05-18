'''
Let's make a game in which user will guess the no. generated
by the pc system betwwen 1 to 100
'''
import random

pc = random.randint(1,100)
# user_guess = None
# print("Your response subbmited successfully")
user_guess = None
count = 0
while pc != user_guess:
    user_guess = int(input("Enter your guess between 1 to 100\n"))
    count = count + 1
    if user_guess == pc:
        print(f"You have guessed the right no. Total attempts taken = {count}")
    else:
        if user_guess < pc:
            print("You have guessed wrong number...Please enter Higher no ")
        else:
            print("You have guessed wrong number...Please enter Lower no ")