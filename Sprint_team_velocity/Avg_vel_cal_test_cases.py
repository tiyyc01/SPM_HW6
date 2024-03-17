import unittest
from Avg_vel_cal import calculate_average_velocity  # Adjust this import based on your project structure.

class TestCalculateAverageVelocity(unittest.TestCase):
    def test_happy_path(self):
        """Test with valid input list."""
        self.assertEqual(calculate_average_velocity([1, 2, 3, 5, 8, 13]), (5.33, None), "Failed to calculate correct average velocity on happy path")
        
    def test_empty_list(self):
        """Test with an empty input list."""
        self.assertEqual(calculate_average_velocity([]), (0, "Error: Empty dataset. Cannot calculate average velocity."), "Failed to handle empty list correctly")
        
    def test_invalid_sprint_points(self):
        """Test with list containing invalid sprint points."""
        self.assertEqual(calculate_average_velocity([1, 4, 9]), (0, "Error: Invalid sprint points. Only specific values are allowed."), "Failed to reject invalid sprint points correctly")
        
    def test_only_allowed_sprint_points(self):
        """Test with list containing only allowed sprint points."""
        self.assertEqual(calculate_average_velocity([20, 40, 100]), (53.33, None), "Failed to handle allowed sprint points correctly")

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCalculateAverageVelocity)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
