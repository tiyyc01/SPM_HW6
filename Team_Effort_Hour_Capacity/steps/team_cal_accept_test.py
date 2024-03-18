from behave import given, when, then
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from team_effort_cal import calculate_individual_effort_hours, calculate_total_effort_hours

@given('"{name}" has {time_off} hours of time off and {commitments} hours of commitments')
def step_impl(context, name, time_off, commitments):
    context.person = {
        "name": name,
        "time_off": float(time_off),
        "commitments": float(commitments),
    }

@given('"{name}"\'s daily availability range is {low} to {high}')
def step_impl(context, name, low, high):
    context.person["daily_availability_range"] = (float(low), float(high))

@when('calculating "{name}"\'s individual effort hours')
def step_impl(context, name):
    person = context.person
    try:
        context.individual_effort_hours = calculate_individual_effort_hours(
            person["name"], person["time_off"], person["commitments"], person["daily_availability_range"]
        )
        context.exception = None
    except Exception as e:
        context.exception = e

@then('the effort hours should be {expected_hours}')
def step_impl(context, expected_hours):
    assert context.exception is None, f"Expected no exception, but got: {context.exception}"
    assert context.individual_effort_hours == float(expected_hours), f"Expected {expected_hours} hours, got {context.individual_effort_hours} hours"

@given('the following team member effort hours')
def step_impl(context):
    context.team_members_effort_hours = {}
    for row in context.table:
        context.team_members_effort_hours[row['name']] = float(row['hours'])

@when('calculating total team effort hours')
def step_impl(context):
    context.total_effort_hours = calculate_total_effort_hours(context.team_members_effort_hours)

@then('the total effort hours should be {expected_hours}')
def step_impl(context, expected_hours):
    assert context.total_effort_hours == float(expected_hours), f"Expected total effort hours to be {expected_hours}, got {context.total_effort_hours}"

@then('an error should be reported stating "{message}"')
def step_impl(context, message):
    assert context.exception is not None, "Expected an exception, but none was raised"
    assert message in str(context.exception), f"Expected error message to include '{message}', but got: '{context.exception}'"
