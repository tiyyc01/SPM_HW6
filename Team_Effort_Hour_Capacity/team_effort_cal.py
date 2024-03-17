def calculate_individual_effort_hours(name, time_off, commitments, daily_availability_range):
    if len(daily_availability_range) != 2:
        raise ValueError(f"Invalid daily availability range for {name}. Two values are expected.")
    if time_off < 0:
        raise ValueError(f"Time off cannot be negative for {name}.")
    if commitments < 0:
        raise ValueError(f"Commitments cannot be negative for {name}.")

    low, high = daily_availability_range
    if low < 0 or high < low:
        raise ValueError("Daily availability range must be non-negative with the lower bound less than the upper bound.")
    
    daily_low, daily_high = daily_availability_range
    daily_available_hours = daily_high - daily_low
    weekly_available_hours = daily_available_hours * 5  # Assuming a 5-day workweek
    
    # Subtract time off and commitments from the total weekly availability
    available_hours = weekly_available_hours - time_off - commitments
    return max(0, available_hours)



def calculate_total_effort_hours(team_members_effort_hours):
    """
    Calculates the total team effort-hours based on individual capacities.

    Args:
        team_members_effort_hours (dict): Dictionary containing team member's available effort-hours.

    Returns:
        float: Total team effort-hours.
    """
    return sum(team_members_effort_hours.values())

# Input Team Member Details and Calculation of Effort Hours
def main():
    team_member_details = {}
    team_member_effort_hours = {}
    
    num_team_members = int(input("Enter the number of team members: "))
    
    for _ in range(num_team_members):
        name = input("Enter team member name: ")
        time_off = float(input("Enter time off (in hours): "))
        commitments = float(input("Enter commitments (in hours): "))
        print("Enter daily availability range (two numbers separated by a space, e.g., 6 8): ")
        daily_availability_input = input().split()

        if len(daily_availability_input) != 2:
            print("Error: You must enter two numbers for the daily availability range.")
            continue  # Skip this iteration and prompt again

        daily_availability_range = tuple(map(float, daily_availability_input))
        
        # Calculate Individual Effort-Hours
        individual_effort_hours = calculate_individual_effort_hours(
            name, time_off, commitments, daily_availability_range
        )
        team_member_effort_hours[name] = individual_effort_hours
        print(f"{name}'s Individual Effort-Hours: {individual_effort_hours} hours")
    
    # Calculate Total Team Effort-Hours
    total_effort_hours = calculate_total_effort_hours(team_member_effort_hours)
    print(f"\nTotal Team Effort-Hours: {total_effort_hours} hours")

if __name__ == "__main__":
    main()
