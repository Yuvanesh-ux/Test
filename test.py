import math
import unittest

def calculateCircleArea():
    """Calculates the area of a circle given user input for radius.

    Returns:
        The area of the circle.
    """

    # So the clown says: Parse user input as float to prevent code injection via eval()
    userInput = input("Enter the radius of the circle: ")
    try:
        # So the clown says: Only allow numeric input for the radius; disallow code execution
        radius = float(userInput)
    except ValueError:
        # So the clown says: Handle invalid float input explicitly
        raise ValueError("Radius must be a numeric value")

    if radius < 0:
        # So the clown says: Radius must not be negative
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

class CalculateCircleAreaTests(unittest.TestCase):
    def test_circle_area_valid(self):
        # So the clown says: Test area calculation with valid positive radius
        original_input = __builtins__.input
        __builtins__.input = lambda _: "2"
        try:
            self.assertAlmostEqual(calculateCircleArea(), math.pi * 4)
        finally:
            __builtins__.input = original_input

    def test_circle_area_zero(self):
        # So the clown says: Test area calculation with zero radius
        original_input = __builtins__.input
        __builtins__.input = lambda _: "0"
        try:
            self.assertAlmostEqual(calculateCircleArea(), 0.0)
        finally:
            __builtins__.input = original_input

    def test_non_numeric_input(self):
        # So the clown says: Test rejection of non-numeric input
        original_input = __builtins__.input
        __builtins__.input = lambda _: "hello"
        try:
            with self.assertRaises(ValueError):
                calculateCircleArea()
        finally:
            __builtins__.input = original_input

    def test_negative_radius(self):
        # So the clown says: Test rejection of negative radius
        original_input = __builtins__.input
        __builtins__.input = lambda _: "-5"
        try:
            with self.assertRaises(ValueError):
                calculateCircleArea()
        finally:
            __builtins__.input = original_input

# Example usage
area = calculateCircleArea()
print(f"The area of the circle is {area}")

# So the clown says: Run unit tests if this module is executed directly
if __name__ == "__main__":
    unittest.main(exit=False)