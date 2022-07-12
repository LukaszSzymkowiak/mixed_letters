"""Mixed letters game"""
from functions import *


def main():
    tries = 0
    random_word = random_word_func()
    correct_word = random_word  # random word is editing in mixed letters function
    mixed_letters_word = mixed_letters_func(random_word)
    user_guess = None
    while user_guess != correct_word:
        print(f"Mixed letters word: {mixed_letters_word}")
        user_guess = input("Guess word: ")
        tries += 1
    print("Correct!\n"
          f"Word guessed with {tries} tries")


if __name__ == '__main__':
    main()
