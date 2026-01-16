Feature: Rock Paper Scissors

  # EXAMPLE SCENARIO (DO NOT DELETE)
  Scenario: Rock beats scissors
    Given player one chooses rock
    And player two chooses scissors
    When the game is played
    Then the result should be player1 wins

  # TODO: Scissors beats paper
  Scenario:
    Given
    And
    When
    Then

  # TODO: Paper beats rock
  Scenario:
    Given
    And
    When
    Then

  # TODO: Draw (player1 == player2)
  Scenario:
    Given
    And
    When
    Then

  # Extension (optional): invalid input should be rejected
  # TODO: Invalid choice
  Scenario:
    Given
    And
    When
    Then
