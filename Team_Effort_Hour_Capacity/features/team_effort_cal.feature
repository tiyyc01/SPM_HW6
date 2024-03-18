Feature: Team Effort Hours Calculation

  Scenario Outline: Calculate individual effort hours for a team member
    Given "<name>" has <time_off> hours of time off and <commitments> hours of commitments
    And "<name>"'s daily availability range is <low> to <high>
    When calculating "<name>"'s individual effort hours
    Then the effort hours should be <expected_hours>

    Examples:
      | name  | time_off | commitments | low | high | expected_hours |
      | Alice | 2        | 5           | 8   | 10   | 35             |
      | Bob   | 8        | 10          | 9   | 17   | 30             |

  Scenario: Calculate total effort hours for the team
    Given the following team member effort hours:
      | name  | hours |
      | Alice | 35    |
      | Bob   | 30    |
    When calculating total team effort hours
    Then the total effort hours should be 65

  Scenario: Handling invalid daily availability range
    Given "Charlie" has 0 hours of time off and 0 hours of commitments
    And "Charlie"'s daily availability range is -1 to 5
    When calculating "Charlie"'s individual effort hours
    Then an error should be reported stating "Daily availability range must be non-negative with the lower bound less than the upper bound."

  Scenario: Handling negative time off
    Given "Dana" has -1 hours of time off and 0 hours of commitments
    And "Dana"'s daily availability range is 8 to 10
    When calculating "Dana"'s individual effort hours
    Then an error should be reported stating "Time off cannot be negative for Dana."

  Scenario: Handling negative commitments
    Given "Eli" has 0 hours of time off and -1 hours of commitments
    And "Eli"'s daily availability range is 8 to 10
    When calculating "Eli"'s individual effort hours
    Then an error should be reported stating "Commitments cannot be negative for Eli."
