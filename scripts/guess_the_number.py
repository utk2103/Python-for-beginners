"""Guess the number — two ways.

Mode 1: the computer picks a number and you guess it.
Mode 2: you pick a number and the computer finds it with binary search.

Run from the repo root:
    python scripts/guess_the_number.py
"""

import math
import random

HUMAN_RANGE = (1, 100)
COMPUTER_RANGE = (1, 1000)


def max_guesses(low, high):
    """Worst-case number of guesses binary search needs for low..high.

    Why: every guess halves the remaining candidates, so after k guesses at
    most 2**k - 1 numbers can be told apart. The smallest k that covers all
            n numbers is ceil(log2(n + 1)) — 7 for 1..100, 10 for 1..1000.
    """
    return math.ceil(math.log2(high - low + 2))


def middle(low, high):
    """The guess that splits low..high into two equal halves."""
    return (low + high) // 2


def narrow(low, high, guess, answer):
    """Shrink the range after hearing 'h' (too high) or 'l' (too low)."""
    if answer == "h":
        return low, guess - 1
    return guess + 1, high


def ask_int(prompt, low, high):
    """Keep asking until the user types a whole number in low..high."""
    while True:
        text = input(prompt).strip()
        try:
            number = int(text)
        except ValueError:
            print(f"'{text}' is not a whole number, try again.")
            continue
        if low <= number <= high:
            return number
        print(f"Please pick a number between {low} and {high}.")


def ask_choice(prompt, choices):
    """Keep asking until the user types one of the allowed letters."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in choices:
            return answer
        print(f"Please type one of: {', '.join(choices)}.")


def play_human_guesses(low, high):
    """Mode 1: the computer thinks of a number, the player guesses."""
    secret = random.randint(low, high)
    print(f"\nI'm thinking of a number between {low} and {high}.")

    attempts = 0
    while True:
        guess = ask_int("Your guess: ", low, high)
        attempts += 1
        if guess > secret:
            print("Too high.")
        elif guess < secret:
            print("Too low.")
        else:
            break

    print(f"Correct! It was {secret}. You needed {attempts} guesses.")
    print(f"Always guessing the middle never takes more than "
          f"{max_guesses(low, high)} guesses.")


def play_computer_guesses(low, high):
    """Mode 2: the player thinks of a number, the computer binary-searches."""
    print(f"\nThink of a number between {low} and {high}. I'll find it in at "
          f"most {max_guesses(low, high)} guesses.")
    input("Press Enter when you're ready...")

    attempts = 0
    while low <= high:
        guess = middle(low, high)
        attempts += 1
        answer = ask_choice(
            f"Is it {guess}? (h = too high, l = too low, c = correct): ",
            ("h", "l", "c"),
        )
        if answer == "c":
            print(f"Got it! Your number is {guess}. "
                  f"That took me {attempts} guesses.")
            return
        low, high = narrow(low, high, guess, answer)

    # Why: an empty range means no number fits every answer given so far
    print("Those answers contradict each other — no number fits them all.")


def main():
    print("Guess the number!")
    print("  1) You guess my number")
    print("  2) I guess your number")
    print("  q) Quit")
    mode = ask_choice("Choose a mode (1/2/q): ", ("1", "2", "q"))

    if mode == "q":
        print("Bye!")
    elif mode == "1":
        play_human_guesses(*HUMAN_RANGE)
    else:
        play_computer_guesses(*COMPUTER_RANGE)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nBye!")
