import unittest
from team_effort_cal import calculate_individual_effort_hours  

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

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCalculateIndividualEffortHours)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
