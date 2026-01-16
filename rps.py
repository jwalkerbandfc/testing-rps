# rps.py

VALID_CHOICES = ("rock", "paper", "scissors")


def normalise_choice(raw: str) -> str:
    """
    Converts user input into a valid choice.
    Raises ValueError if the input is not rock/paper/scissors.
    """
    if raw is None:
        raise ValueError("Choice cannot be empty")

    choice = raw.strip().lower()

    # Allow short forms
    shortcuts = {"r": "rock", "p": "paper", "s": "scissors"}
    choice = shortcuts.get(choice, choice)

    if choice not in VALID_CHOICES:
        raise ValueError(f"Invalid choice: {raw}")

    return choice


def play(player1: str, player2: str) -> str:
    """
    Core game logic (pure function, ideal for automated tests).
    Returns one of:
      - "draw"
      - "player1 wins"
      - "player2 wins"
    Raises ValueError for invalid inputs.
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
    Converts a menu input into an integer 1 or 2.
    Raises ValueError if invalid.
    """
    if raw is None:
        raise ValueError("Menu choice cannot be empty")
    s = raw.strip()
    if s not in ("1", "2"):
        raise ValueError("Menu choice must be 1 or 2")
    return int(s)


def run_game() -> None:
    print("Rock–Paper–Scissors")
    print("-------------------")

    while True:
        print("\nMenu:")
        print("1) Play a round")
        print("2) Quit")

        try:
            menu = get_menu_choice(input("Select an option (1-2): "))
        except ValueError as e:
            print(f"Invalid menu choice. {e}")
            continue

        if menu == 2:
            print("Goodbye!")
            break

        # menu == 1
        try:
            p1 = input("Player 1 - choose Rock/Paper/Scissors (or r/p/s): ")
            p2 = input("Player 2 - choose Rock/Paper/Scissors (or r/p/s): ")
            result = play(p1, p2)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Invalid input. {e}")


def main() -> None:
    run_game()


if __name__ == "__main__":
    main()
