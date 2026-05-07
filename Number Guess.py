import random
number = random.randint(1,100)
attempts=0
while True:
    guess=int (input("Guess any number between 1 to 100:"))
    attempts =+1
    if guess < number :
        print("TOO LOW TRY SOMETHING HIGHER")
    elif guess > number :
        print ("TOO HIGH TRY SOMETHING LOWER")
    else :
        print (" CONGRATS YOU GUESSED THE NUMBER IN", attempts, "ATTEMPTS")
