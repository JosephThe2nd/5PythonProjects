import random

top_of_range = input("Please type a number! ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number greater than 0 next time! ")
        quit()
else:
    print("Please type a number next time! ")
    quit()

random_numer = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Please make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time! ")
        continue

    if user_guess == random_numer:
        print("You guessed it in", guesses,  "tries")
        break 
    elif user_guess > random_numer:
            print("You was above the number ")
    else: print("You were below the number")   
        
        
         






    