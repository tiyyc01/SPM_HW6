def calculate_individual_effort_hours(name, time_off, commitments, daily_availability_range):
    """
    Calculates the available effort-hours for an individual team member.

    Args:
        name (str): The name of the team member.
        time_off (float): The number of hours the team member is off during a sprint.
        commitments (float): The time commitments of the team member to various ceremonies during a sprint (in hours).
        daily_availability_range (tuple[float, float]): The low and high bounds of the daily availability range in hours.

    Returns:
        float: Available effort-hours for the team member.
    """

    try:
        # Ensure range is valid
        if daily_availability_range[0] < 0 or daily_availability_range[1] <= daily_availability_range[0]:
            raise ValueError("Daily availability range must be non-negative with lower bound less than or equal to upper bound.")

        # Calculate possible effort hours within the range
        possible_effort_hours = [daily_availability - time_off - commitments for daily_availability in daily_availability_range]

        # Return maximum available effort hours while ensuring non-negativity
        return max(0, max(possible_effort_hours))

    except Exception as e:
        raise ValueError(f"Error calculating individual effort-hours for {name}: {str(e)}")


def calculate_total_effort_hours(team_members):
    """
    Calculates the total team effort-hours based on individual capacities.

    Args:
        team_members (dict): Dictionary containing team member details.

    Returns:
        float: Total team effort-hours.
    """

    try:
        total_effort_hours = sum(team_members.values())
        return total_effort_hours

    except Exception as e:
        raise ValueError(f"Error calculating total team effort-hours: {str(e)}")


# Input Team Member Details
team_member_details = {}
num_team_members = int(input("Enter the number of team members: "))

for _ in range(num_team_members):
    name = input("Enter team member name: ")
    time_off = float(input("Enter time off (in hours): "))
    commitments = float(input("Enter commitments (in hours): "))
    print("Enter daily availability range (separated by a space, e.g., 6 8): ")
    daily_availability_range = tuple(map(float, input().split()))

    team_member_details[name] = {
        "time_off": time_off,
        "commitments": commitments,
        "daily_availability_range": daily_availability_range
    }

# Calculate Individual Effort-Hours
for name, details in team_member_details.items():
    individual_effort_hours = calculate_individual_effort_hours(
        name, details["time_off"], details["commitments"], details["daily_availability_range"]
    )
    print(f"{name}'s Individual Effort-Hours: {individual_effort_hours} hours")

# Calculate Total Team Effort-Hours
total_effort_hours = calculate_total_effort_hours({
    name: calculate_individual_effort_hours(name, details["time_off"], details["commitments"], details["daily_availability_range"])
    for name, details in team_member_details.items()
})
print(f"\nTotal Team Effort-Hours: {total_effort_hours} hours")
