import unittest
from team_effort_cal import calculate_individual_effort_hours,calculate_total_effort_hours

class TestCalculateTotalEffortHours(unittest.TestCase):
    def test_total_effort_hours_happy_path(self):
        """Happy path: Proper calculation with valid inputs."""
        team_members_effort_hours = {
            'John': 40,
            'Jane': 35,
            'Doe': 25
        }
        self.assertEqual(
            calculate_total_effort_hours(team_members_effort_hours),
            100,  # Expected total effort-hours: 40 + 35 + 25
            "Failed to calculate total effort hours correctly for valid inputs."
        )

    def test_total_effort_hours_empty_input(self):
        """Unhappy path: No team members provided."""
        team_members_effort_hours = {}
        self.assertEqual(
            calculate_total_effort_hours(team_members_effort_hours),
            0,  # Expected total effort-hours: 0 for empty input
            "Failed to handle empty input correctly for total effort hours calculation."
        )

class TestCalculateIndividualEffortHours(unittest.TestCase):
    def test_happy_path(self):
        """Happy path: Proper calculation with valid inputs."""
        # Corrected expected output to match the accurate calculation
        self.assertEqual(
            calculate_individual_effort_hours("John", 1, 2, (8, 10)),
            7,  # (10 - 8) * 5 - 1 - 2 = 7
            "The calculation of effort hours did not match expected output."
        )


    def test_invalid_daily_range(self):
        """Unhappy path: Invalid daily availability range."""
        with self.assertRaises(ValueError):
            calculate_individual_effort_hours("Jane", 1, 2, (8, 7))
    
    def test_negative_time_off(self):
        """Unhappy path: Negative time off."""
        with self.assertRaises(ValueError):
            calculate_individual_effort_hours("Joe", -1, 2, (8, 10))
    
    
    def test_single_value_range(self):
        """Unhappy path: Daily availability range with only one value."""
        with self.assertRaises(ValueError):
            calculate_individual_effort_hours("Jake", 1, 2, (8,))
    
    def test_negative_daily_range(self):
        """Unhappy path: Negative values in daily availability range."""
        with self.assertRaises(ValueError):
            calculate_individual_effort_hours("Jill", 1, 2, (-8, -6))
    
    def test_zero_effort_hours(self):
        """Boundary condition: Zero effort hours when time off and commitments equal daily hours."""
        self.assertEqual(
            calculate_individual_effort_hours("Jack", 1, 14, (8, 10)),
            0,  # (10 - 8) * (5 - 1) - 14 = 0
            "Expected zero effort hours, but got a different result."
        )

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCalculateIndividualEffortHours))
    suite.addTest(unittest.makeSuite(TestCalculateTotalEffortHours))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())