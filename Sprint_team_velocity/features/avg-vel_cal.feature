Feature: Calculate Average Velocity
  As a team, we want to calculate our average velocity based on completed sprint points so that we can estimate future sprint capacities more accurately.

  Scenario Outline: Calculate average velocity with valid sprint points
    Given the user has entered sprint points "<sprint_points>"
    When the system calculates the average velocity
    Then the system should return an average velocity of "<average_velocity>"

    Examples:
      | sprint_points      | average_velocity |
      | 5, 8, 13, 20       | 11.5             |
      | 1, 2, 3, 5, 8, 13  | 5.33             |
      | 20, 40, 100        | 53.33            |

  Scenario: Handle invalid sprint points input
    Given the user has entered sprint points "4, 7, 15"
    When the system calculates the average velocity
    Then the system should return an error message about invalid sprint points

  Scenario: Handle empty sprint points input
    Given the user has entered no sprint points
    When the system calculates the average velocity
    Then the system should return an error message about empty dataset
