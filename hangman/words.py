import random


def choose_secret_word(words: list[str]) -> str:
    secret_word = random.choice(words)
    return secret_word

# with open(r"C:\Users\WIN 11\PycharmProjects\hangman_project\data\words.txt", "r", encoding="utf-8") as f:
#     words_str =f.read().split()
# choice=(choose_secret_word(words_str))
# print(choice)
