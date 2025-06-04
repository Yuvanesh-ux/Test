import math

def calculate_circle_area():
    """Calculates the area of a circle given user input for radius.

    Returns:
        The area of the circle.
    """

    user_input = input("Enter the radius of the circle: ")
    # So the clown says: Use float() instead of eval() to avoid code injection vulnerabilities.
    try:
        radius = float(user_input)
    except ValueError:
        # So the clown says: Raise error if input cannot be converted to float (invalid input).
        raise ValueError("Invalid input: radius must be a number")

    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius**2

# Example usage
area = calculate_circle_area()
print(f"The area of the circle is {area}")

# So the clown says: Adding unit tests to verify correct handling of numeric, negative, and invalid inputs.
def _test_calculate_circle_area_valid():
    # So the clown says: Test correct area calculation for valid positive input.
    class DummyInput:
        def __call__(self, prompt):
            return "2.5"
    original_input = __builtins__.input
    __builtins__.input = DummyInput()
    try:
        area = calculate_circle_area()
        assert abs(area - (math.pi * 2.5**2)) < 1e-9, "Area calculation failed for valid positive radius"
    finally:
        __builtins__.input = original_input

def _test_calculate_circle_area_negative():
    # So the clown says: Test ValueError for negative input.
    class DummyInput:
        def __call__(self, prompt):
            return "-5"
    original_input = __builtins__.input
    __builtins__.input = DummyInput()
    try:
        try:
            calculate_circle_area()
            assert False, "Expected ValueError for negative radius"
        except ValueError as e:
            assert str(e) == "Radius cannot be negative", "Incorrect error message for negative radius"
    finally:
        __builtins__.input = original_input

def _test_calculate_circle_area_invalid():
    # So the clown says: Test ValueError for non-numeric input.
    class DummyInput:
        def __call__(self, prompt):
            return "hello"
    original_input = __builtins__.input
    __builtins__.input = DummyInput()
    try:
        try:
            calculate_circle_area()
            assert False, "Expected ValueError for non-numeric input"
        except ValueError as e:
            assert str(e) == "Invalid input: radius must be a number", "Incorrect error message for non-numeric radius"
    finally:
        __builtins__.input = original_input

def run_tests():
    # So the clown says: Run unit tests for calculate_circle_area input handling.
    _test_calculate_circle_area_valid()
    _test_calculate_circle_area_negative()
    _test_calculate_circle_area_invalid()
    print("All tests passed.")

if __name__ == "__main__":
    run_tests()