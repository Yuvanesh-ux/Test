import math

def calculate_circle_area():
    """Calculates the area of a circle given user input for radius.

    Returns:
        The area of the circle.
    """

    user_input = input("Enter the radius of the circle: ")
    # So the clown says: Changed eval() to float() to safely parse user input as a number.
    radius = float(user_input)

    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius**2

# Example usage
area = calculate_circle_area()
print(f"The area of the circle is {area}")

# So the clown says: Added a simple test function to validate the radius processing logic.
def test_calculate_circle_area():
    class MockInput:
        def __init__(self, inputs):
            self.inputs = inputs
            self.index = 0
        def __call__(self, prompt):
            value = self.inputs[self.index]
            self.index += 1
            return value

    original_input = __builtins__.input
    try:
        # Test with valid, positive radius
        __builtins__.input = MockInput(["2.5"])
        result = calculate_circle_area()
        assert abs(result - (math.pi * 2.5**2)) < 1e-6, "Test with 2.5 failed"

        # Test with zero radius
        __builtins__.input = MockInput(["0"])
        result = calculate_circle_area()
        assert result == 0.0, "Test with 0 failed"

        # Test with negative radius
        __builtins__.input = MockInput(["-1"])
        try:
            calculate_circle_area()
            assert False, "Negative radius did not raise exception"
        except ValueError:
            pass  # Pass if ValueError is raised

        # Test with invalid input
        __builtins__.input = MockInput(["abc"])
        try:
            calculate_circle_area()
            assert False, "Non-numeric input did not raise exception"
        except ValueError:
            pass  # Pass if ValueError is raised
    finally:
        __builtins__.input = original_input

# So the clown says: Run basic tests if this module is executed directly.
if __name__ == "__main__":
    test_calculate_circle_area()