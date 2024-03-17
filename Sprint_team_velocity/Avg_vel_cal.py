allowed_sprint_points = {1, 2, 3, 5, 8, 13, 20, 40, 100}

def calculate_average_velocity(sprint_points):
    if not sprint_points:
        return 0, "Error: Empty dataset. Cannot calculate average velocity."
    
    if not all(point in allowed_sprint_points for point in sprint_points):
        return 0, "Error: Invalid sprint points. Only specific values are allowed."

    try:
        total_points = sum(sprint_points)
        number_of_sprints = len(sprint_points)
        average_velocity = total_points / number_of_sprints
        return round(average_velocity, 2), None
    except Exception as e:
        return 0, f"Error: {str(e)}. Unable to calculate average velocity."


# User Input
sprint_points_input = input("Enter sprint points as a list (e.g., 1, 2, 3, 5, 8, 13, 20, 40, 100): ")

try:
    # Parse Input
    input_points = [int(point.strip()) for point in sprint_points_input.split(',')]
    invalid_points = [point for point in input_points if point not in allowed_sprint_points]
    
    if invalid_points:
        # If there are any invalid points, print an error message and stop the program
        print(f"Input Error: Invalid sprint points {invalid_points}. Allowed points are {sorted(list(allowed_sprint_points))}.")
    else:
        # Calculate Average Velocity
        result = calculate_average_velocity(input_points)

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
