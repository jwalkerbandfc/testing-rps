# tdd_test.py
import pytest
from rps import play, normalise_choice, get_menu_choice

# EXAMPLE TEST (DO NOT DELETE)
def test_rock_beats_scissors():
    assert play("rock", "scissors") == "player1 wins"


# TODO: Write tests for the remaining win rules
def test_scissors_beats_paper():
    pass

def test_paper_beats_rock():
    pass


# TODO: Write a test for DRAW logic (player1 == player2)
def test_draw_when_same_choice():
    pass


# --- Extension tests (recommended) ---

# EXAMPLE EXTENSION TEST (DO NOT DELETE)
def test_normalise_choice_accepts_shortcut_r():
    assert normalise_choice("r") == "rock"


# TODO: Write one test that checks invalid input raises ValueError
def test_invalid_choice_raises_value_error():
    pass


# TODO: Write one test for menu validation (1 or 2 only)
def test_menu_choice_invalid_raises_value_error():
    pass
