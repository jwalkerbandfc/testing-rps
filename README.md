# Rock–Paper–Scissors: Automated Testing with TDD and BDD (Python)

## Overview
This activity introduces automated testing through a simple Rock–Paper–Scissors (RPS) program. You will work with two complementary testing approaches:

- **Test-Driven Development (TDD)** using the `pytest` framework (logic-focused, unit testing)
- **Behaviour-Driven Development (BDD)** using the `behave` framework (scenario-focused, acceptance/behaviour testing)

The codebase includes a **console menu system** to simulate real program interaction. However, your automated tests should primarily target **testable functions** rather than interactive input loops.

---

## Learning Outcomes
By completing this task, you should be able to:

1. Explain the purpose of automated testing frameworks.
2. Write unit tests using `pytest` to validate core game logic.
3. Write behaviour scenarios using Gherkin syntax and execute them with `behave`.
4. Produce tests that cover **all win conditions and the draw condition**.
5. Extend test coverage to include input validation (recommended extension).

---

## Game Rules (All Must Be Tested)
- Rock beats Scissors  
- Scissors beats Paper  
- Paper beats Rock  
- **If both players choose the same option, the result is a draw**  

The draw rule is implemented as `player1 == player2` and **must be tested**.

---

## Project Structure
Create the following files:

rps_project/ │ ├── rps.py ├── tdd_test.py ├── rps.feature └── bdd_test.py

---

## File 1: `rps.py` (Provided – Do Not Modify)

This file contains:
- Core game logic designed for automated testing
- Input validation and normalisation
- A simple interactive menu system

```python
# rps.py

VALID_CHOICES = ("rock", "paper", "scissors")


def normalise_choice(raw: str) -> str:
    """
    Converts user input into a valid choice.
    Accepts rock/paper/scissors or shortcuts r/p/s.
    Raises ValueError if invalid.
    """
    if raw is None:
        raise ValueError("Choice cannot be empty")

    choice = raw.strip().lower()
    shortcuts = {"r": "rock", "p": "paper", "s": "scissors"}
    choice = shortcuts.get(choice, choice)

    if choice not in VALID_CHOICES:
        raise ValueError(f"Invalid choice: {raw}")

    return choice


def play(player1: str, player2: str) -> str:
    """
    Core game logic (pure function).
    Returns:
      - "draw"
      - "player1 wins"
      - "player2 wins"
    """
    p1 = normalise_choice(player1)
    p2 = normalise_choice(player2)

    if p1 == p2:
        return "draw"

    wins = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock",
    }

    return "player1 wins" if wins[p1] == p2 else "player2 wins"


def get_menu_choice(raw: str) -> int:
    """
    Validates menu input (1 or 2).
    """
    if raw is None:
        raise ValueError("Menu choice cannot be empty")

    value = raw.strip()
    if value not in ("1", "2"):
        raise ValueError("Menu choice must be 1 or 2")

    return int(value)


def run_game() -> None:
    """
    Interactive menu system.
    Automated tests should NOT test this function directly.
    """
    print("Rock–Paper–Scissors")
    print("-------------------")

    while True:
        print("\nMenu:")
        print("1) Play a round")
        print("2) Quit")

        try:
            menu = get_menu_choice(input("Select an option (1-2): "))
        except ValueError as e:
            print(f"Invalid menu choice: {e}")
            continue

        if menu == 2:
            print("Goodbye!")
            break

        try:
            p1 = input("Player 1 - choose Rock/Paper/Scissors (or r/p/s): ")
            p2 = input("Player 2 - choose Rock/Paper/Scissors (or r/p/s): ")
            result = play(p1, p2)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Invalid input: {e}")


def main() -> None:
    run_game()


if __name__ == "__main__":
    main()
