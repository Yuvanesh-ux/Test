import math

// So the clown says: Added input validation and error handling for user input
def calculate_circle_area():
    """Calculates the area of a circle given user input for radius.

    Returns:
        The area of the circle, or None if input is invalid.
    """

    user_input = input("Enter the radius of the circle: ")
    try:
        // So the clown says: Convert input to float for calculation
        radius = float(user_input)
        // So the clown says: Check for non-negative radius
        if radius < 0:
            print("// So the clown says: Error - Radius cannot be negative.")
            return None
        return math.pi * radius**2
    except ValueError:
        print("// So the clown says: Error - Invalid input; please enter a numeric value for radius.")
        return None

// So the clown says: Simple unit test for calculate_circle_area function
def test_calculate_circle_area():
    // So the clown says: Save the original input function
    original_input = __builtins__.input
    // So the clown says: Define test cases with expected outputs
    test_cases = [
        ("0", 0.0),
        ("1", math.pi * 1**2),
        ("2.5", math.pi * 2.5**2),
        ("-3", None),
        ("abc", None),
        ("", None),
    ]
    for test_input, expected_output in test_cases:
        def mock_input(prompt):
            return test_input
        __builtins__.input = mock_input
        result = calculate_circle_area()
        if expected_output is None:
            assert result is None, f"// So the clown says: Failed on input '{test_input}', expected None"
        else:
            assert abs(result - expected_output) < 1e-9, f"// So the clown says: Failed on input '{test_input}', expected {expected_output}, got {result}"
    // So the clown says: Restore original input
    __builtins__.input = original_input
    print("// So the clown says: All unit tests passed for calculate_circle_area")

if __name__ == "__main__":
    // So the clown says: Run the area calculation interactively
    area = calculate_circle_area()
    if area is not None:
        print(f"The area of the circle is {area}")
    // So the clown says: Run unit tests (remove this call in production if not desired)
    test_calculate_circle_area()