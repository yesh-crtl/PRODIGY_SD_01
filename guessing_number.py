import random

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess the number (1 to 100): "))
    attempts += 1

    if guess > secret_number:
        print("Too high!")

    elif guess < secret_number:
        print("Too low!")

    else:
        print(f"Correct! You guessed the number in {attempts} attempts.")
        break
