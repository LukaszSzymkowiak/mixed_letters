import random
from words import words


def random_word_func():
    return random.choice(words)


def mixed_letters_func(random_word):
    mixed_letters_word = ""
    while len(random_word) != 0:
        random_index = random.randrange(len(random_word))
        mixed_letters_word += random_word[random_index]
        random_word = random_word[:random_index] + random_word[random_index + 1:]
    return mixed_letters_word
