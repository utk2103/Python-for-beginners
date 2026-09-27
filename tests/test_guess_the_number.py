"""Tests for scripts/guess_the_number.py.

Run from the repo root:
    python -m unittest discover tests
"""

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from scripts.guess_the_number import (
    ask_choice,
    ask_int,
    main,
    max_guesses,
    middle,
    narrow,
    play_computer_guesses,
    play_human_guesses,
)


def run_with_input(func, typed, *args):
    """Call func as if the user typed each item of `typed` in order.

    Returns (what func returned, everything it printed).
    Why: the game talks through input() and print(), so tests swap in
    fake keystrokes and capture the screen instead of needing a person.
    """
    screen = io.StringIO()
    with patch("builtins.input", side_effect=typed), redirect_stdout(screen):
        result = func(*args)
    return result, screen.getvalue()


class TestMaxGuesses(unittest.TestCase):
    def test_known_ranges(self):
        self.assertEqual(max_guesses(1, 100), 7)
        self.assertEqual(max_guesses(1, 1000), 10)

    def test_single_number_needs_one_guess(self):
        self.assertEqual(max_guesses(5, 5), 1)


class TestMiddle(unittest.TestCase):
    def test_splits_range(self):
        self.assertEqual(middle(1, 100), 50)
        self.assertEqual(middle(51, 100), 75)

    def test_single_number(self):
        self.assertEqual(middle(7, 7), 7)


class TestNarrow(unittest.TestCase):
    def test_too_high_keeps_lower_half(self):
        self.assertEqual(narrow(1, 100, 50, "h"), (1, 49))

    def test_too_low_keeps_upper_half(self):
        self.assertEqual(narrow(1, 100, 50, "l"), (51, 100))

    def test_contradiction_leaves_empty_range(self):
        low, high = narrow(6, 6, 6, "h")
        self.assertGreater(low, high)

    def test_binary_search_finds_every_number_in_time(self):
        # Why: proves the ~log2(n) promise for every possible secret,
        # not just the few we'd think to type by hand.
        for secret in range(1, 1001):
            low, high, guesses = 1, 1000, 0
            while True:
                guess = middle(low, high)
                guesses += 1
                if guess == secret:
                    break
                answer = "h" if guess > secret else "l"
                low, high = narrow(low, high, guess, answer)
            self.assertLessEqual(guesses, max_guesses(1, 1000))


class TestAskInt(unittest.TestCase):
    def test_accepts_valid_number(self):
        number, _ = run_with_input(ask_int, ["42"], "> ", 1, 100)
        self.assertEqual(number, 42)

    def test_reprompts_on_text(self):
        number, screen = run_with_input(ask_int, ["abc", "7"], "> ", 1, 100)
        self.assertEqual(number, 7)
        self.assertIn("'abc' is not a whole number", screen)

    def test_reprompts_out_of_range(self):
        number, screen = run_with_input(ask_int, ["0", "101", "100"], "> ", 1, 100)
        self.assertEqual(number, 100)
        self.assertEqual(screen.count("Please pick a number between 1 and 100."), 2)


class TestAskChoice(unittest.TestCase):
    def test_accepts_valid_choice(self):
        choice, _ = run_with_input(ask_choice, ["h"], "> ", ("h", "l", "c"))
        self.assertEqual(choice, "h")

    def test_ignores_case_and_spaces(self):
        choice, _ = run_with_input(ask_choice, ["  C "], "> ", ("h", "l", "c"))
        self.assertEqual(choice, "c")

    def test_reprompts_on_invalid_choice(self):
        choice, screen = run_with_input(ask_choice, ["x", "l"], "> ", ("h", "l", "c"))
        self.assertEqual(choice, "l")
        self.assertIn("Please type one of: h, l, c.", screen)


class TestPlayHumanGuesses(unittest.TestCase):
    @patch("scripts.guess_the_number.random.randint", return_value=42)
    def test_hints_and_counts_attempts(self, _randint):
        _, screen = run_with_input(play_human_guesses, ["50", "25", "42"], 1, 100)
        self.assertIn("Too high.", screen)
        self.assertIn("Too low.", screen)
        self.assertIn("Correct! It was 42. You needed 3 guesses.", screen)

    @patch("scripts.guess_the_number.random.randint", return_value=42)
    def test_bad_input_is_not_counted(self, _randint):
        _, screen = run_with_input(play_human_guesses, ["abc", "42"], 1, 100)
        self.assertIn("You needed 1 guesses.", screen)


class TestPlayComputerGuesses(unittest.TestCase):
    def test_guesses_right_away(self):
        # "" is the Enter press before the game starts.
        _, screen = run_with_input(play_computer_guesses, ["", "c"], 1, 1000)
        self.assertIn("Your number is 500. That took me 1 guesses.", screen)

    def test_worst_case_stays_within_limit(self):
        answers = [""] + ["l"] * 9 + ["c"]
        _, screen = run_with_input(play_computer_guesses, answers, 1, 1000)
        self.assertIn("Your number is 1000. That took me 10 guesses.", screen)

    def test_detects_contradiction(self):
        answers = [""] + ["h"] * 10
        _, screen = run_with_input(play_computer_guesses, answers, 1, 1000)
        self.assertIn("Those answers contradict each other", screen)


class TestMain(unittest.TestCase):
    @patch("scripts.guess_the_number.play_human_guesses")
    def test_mode_1_starts_human_game(self, play):
        run_with_input(main, ["1"])
        play.assert_called_once_with(1, 100)

    @patch("scripts.guess_the_number.play_computer_guesses")
    def test_mode_2_starts_computer_game(self, play):
        run_with_input(main, ["2"])
        play.assert_called_once_with(1, 1000)

    def test_quit(self):
        _, screen = run_with_input(main, ["q"])
        self.assertIn("Bye!", screen)

    @patch("scripts.guess_the_number.play_human_guesses")
    def test_invalid_mode_reprompts(self, play):
        _, screen = run_with_input(main, ["3", "1"])
        self.assertIn("Please type one of: 1, 2, q.", screen)
        play.assert_called_once()


if __name__ == "__main__":
    unittest.main()
