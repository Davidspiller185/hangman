

def init_state(secret: str, max_tries: int) -> dict:
  dictionary=  {
        "secret": secret, # המילה הסודית
        "display": ["_" for _ in secret],  # רשימת תווים לתצוגה, "_"
        "guessed": set(),  # אותיות שנוחשו
        "wrong_guesses": 0,  # כמה טעויות בוצעו
        "max_tries": max_tries  # מגבלה
    }
  return dictionary


def validate_guess(ch: str, guessed: set[str]) -> tuple[bool, str]:
    if len(ch)==1 and ch not in guessed and ch.isalpha():
        return True,"the choice is correct"
    else:
        return False,"the choice is incorrect "

def apply_guess(state: dict, ch: str) -> bool:
    found=False
    for i,letter in enumerate((state["secret"])):
        if ch == letter:
           state["display"][i]=ch
           found=True
    state["guessed"].add(ch)
    if found:
        print("You succeeded in your guessed ")
        return True
    else:
        print("You failed in your guessed ")
        state["wrong_guesses"]+=1
        return False

def is_won(state: dict) -> bool:
    if "".join(state["display"])==state["secret"]:
        return True
    else:
        return False
def is_lost(state: dict) -> bool:
    if state["wrong_guesses"] >= state["max_tries"]:
        return True
    else:
        return False
def render_display(state: dict) -> str:
    return state["display"]

def render_summary(state: dict) -> str:
    return f"final summary:{state["secret"]} + {state["guessed"]}"


