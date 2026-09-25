# guess_game.py
import random

def main():
    # Generate a random secret number between 1 and 10
    secret_number = random.randint(1, 10)
    guess = None

    print("Welcome to the Guessing Game! Try to guess the secret number between 1 and 10.")

    # Loop keeps running until the user guesses correctly
    while guess != secret_number:
        guess = int(input("Enter your guess: "))

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed it right! 🎉")

if __name__ == "__main__":
    main()