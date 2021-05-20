import time
import random

print("""
**************************************
NUMBER PREDİCTİON

Guess a number between 1 and 100.
**************************************
""")
random_number = random.randint(1,100)
# it produces a random number between a given range
number_of_predictions = 10
while True:
    guess = int(input("Enter your guess: "))

    if (guess < random_number):
        if abs(guess - random_number) > 10:
            print("Cold") #say cold if the guess is far than 10
        else:
            print("warm")
        print("Informations are being questioned.")
        time.sleep(1)
        print("Please guess more a higher number....")
        number_of_predictions -=1 # num of estimation right decreases


    elif (guess > random_number):
        if abs(guess - random_number) > 10:
            print("Cold") # say cold if the guess is far than 10
        else:
            print("warm")
        print("Informations are being questioned.")
        time.sleep(1)
        print("Please guess lower a number....")
        number_of_predictions -=1 # num of estimation right decreases
    else:
        print("Informations are being questioned.")
        time.sleep(1)
        print("Congratulations!!! The number is : ", random_number)
        break

    if number_of_predictions == 0 :
        print("Your guessing right is over")
        print("The number is : ", random_number)
        break