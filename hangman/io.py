from hangman.game import is_won,render_display,is_lost,render_summary



def prompt_guess() -> str:

    letter=input("Enter a letter please ")
    return letter

def print_status(state: dict) -> None:
    display=render_display(state)
    print(display)
    print(state["guessed"])
    guesses_remaining=state["max_tries"] - state["wrong_guesses"]
    print(guesses_remaining)

def  print_result(state: dict) -> None:
    summary = render_summary(state)
    if is_won(state):
        print("you win" + summary)
    if is_lost(state):
        print("You failed" + summary)










