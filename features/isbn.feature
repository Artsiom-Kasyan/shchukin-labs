Feature: ISBN-10 verification
  Scenario Outline: Check a printed book identifier
    Given the printed ISBN "<isbn>"
    When the reader verifies the identifier
    Then the result is <result>

    Examples:
      | isbn          | result  |
      | 0-306-40615-2 | valid   |
      | 0306406153    | invalid |
      | 306406152     | invalid |
      | 080442957X    | valid   |
