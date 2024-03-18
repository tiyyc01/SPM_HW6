from behave import given, when, then
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from Avg_vel_cal import calculate_average_velocity


@given('the user has entered sprint points "{sprint_points}"')
def step_given_user_enters_sprint_points(context, sprint_points):
    # Handles normal input by converting string to list of integers
    context.sprint_points = [int(point.strip()) for point in sprint_points.split(',')]

@given('the user has entered no sprint points')
def step_given_user_enters_no_sprint_points(context):
    # Handles the case where no sprint points are entered
    context.sprint_points = []

@when('the system calculates the average velocity')
def step_when_system_calculates_velocity(context):
    # Calls the calculate_average_velocity function and stores the output
    context.average_velocity, context.error_message = calculate_average_velocity(context.sprint_points)

@then('the system should return an average velocity of "{average_velocity}"')
def step_then_system_returns_velocity(context, average_velocity):
    # Checks if the returned average velocity matches the expected value
    assert str(context.average_velocity) == average_velocity, f"Expected {average_velocity}, got {context.average_velocity}"

@then('the system should return an error message about invalid sprint points')
def step_then_system_returns_error_invalid_points(context):
    # Checks if the error message for invalid sprint points is correct
    expected_error = "Error: Invalid sprint points. Only specific values are allowed."
    assert context.error_message == expected_error, f"Expected '{expected_error}', got '{context.error_message}'"

@then('the system should return an error message about empty dataset')
def step_then_system_returns_error_empty_dataset(context):
    # Checks if the error message for an empty dataset is correct
    expected_error = "Error: Empty dataset. Cannot calculate average velocity."
    assert context.error_message == expected_error, f"Expected '{expected_error}', got '{context.error_message}'"