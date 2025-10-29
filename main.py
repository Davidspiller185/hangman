from hangman.words import choose_secret_word
from hangman.game import init_state,is_won,is_lost,validate_guess,apply_guess,render_display
from hangman.io import prompt_guess, print_status,print_result


def play(words: list[str], max_tries: int = 6) -> None:
    choice = choose_secret_word(words)
    print(choice)
    dic=init_state(choice,max_tries)

    while not is_lost(dic) and not is_won(dic) :
        letter = prompt_guess()
        valid,msg=validate_guess(letter,dic["guessed"])
        print(msg)
        if not valid:
            continue
        apply_guess(dic, letter)
        print(render_display(dic))

    print_status(dic)
    print_result(dic)
if __name__ == "__main__":
    with open(r"C:\Users\WIN 11\PycharmProjects\hangman_project\data\words.txt", "r", encoding="utf-8") as f:
        words_str = [w.strip() for w in f.read().split() if w.strip()]
    play(words_str)