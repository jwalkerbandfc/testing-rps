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
