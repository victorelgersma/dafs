import random

secret_number = random.randint(1,20)

attempts = 5
while True:
    if (attempts > 0 ):
        print(f"you have {attempts} attempts left")
        attempts = attempts -1
        guess = int(input("Guess the number"))
        if secret_number > guess:
            print("Too low")
        elif secret_number < guess:
            print("Too high!")
        else:
            break
    else:
        print("You lose!")

print("Correct guess")

print(f"secret number is {secret_number}")