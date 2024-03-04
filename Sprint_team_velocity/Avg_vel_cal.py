def calculate_average_velocity(sprint_points):
    """
    Calculate the average velocity based on the provided sprint points.

    Args:
    - sprint_points (list): List containing sprint point completions.

    Returns:
    - Tuple: (float, str) representing (Average velocity, Error message).
    """
    if not sprint_points:
        return 0, "Error: Empty dataset. Cannot calculate average velocity."

    try:
        total_points = sum(sprint_points)
        number_of_sprints = len(sprint_points)
        average_velocity = total_points / number_of_sprints
        return round(average_velocity, 2), None
    except Exception as e:
        return 0, f"Error: {str(e)}. Unable to calculate average velocity."

# UserInput
sprint_points_input = input("Enter sprint points as a list (e.g., 1, 2, 3, 5, 8, 13): ")

try:
    # Parse Input
    sample_sprint_points = [int(point) for point in sprint_points_input.split(',')]

    # Calculate Average Velocity
    result = calculate_average_velocity(sample_sprint_points)

    # Print Results
    average_velocity, error_message = result
    if error_message:
        print(error_message)
    else:
        print(f"Average Velocity: {average_velocity}")

except ValueError as input_error:
    print(f"Input Error: {str(input_error)}")
except Exception as other_error:
    print(f"Unexpected Error: {str(other_error)}")
