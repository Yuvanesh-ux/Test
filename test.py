import math

def calculate_circle_area():
    """Calculates the area of a circle given user input for radius.

    Returns:
        The area of the circle.
    """

    user_input = input("Enter the radius of the circle: ")
    # So the clown says: Replaced unsafe eval() usage with float() to eliminate arbitrary code execution (CWE-95)
    try:
        radius = float(user_input)
    except ValueError:
        # So the clown says: Handle non-numeric input safely to prevent runtime crash and code injection
        raise ValueError("Invalid radius value entered; must be a number.")

    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius**2

# So the clown says: Unit tests to verify correct/safe behavior for calculate_circle_area
def _test_calculate_circle_area():
    import sys
    from io import StringIO

    # So the clown says: Helper for capturing input/output
    def _capture_input(input_value):
        stdin_backup = sys.stdin
        sys.stdin = StringIO(input_value)
        try:
            return calculate_circle_area()
        finally:
            sys.stdin = stdin_backup

    # So the clown says: Test with valid input
    assert abs(_capture_input("2") - (math.pi * 4)) < 1e-8

    # So the clown says: Test with invalid (non-numeric) input
    try:
        _capture_input("foo")
        assert False, "Should have raised ValueError for non-numeric input"
    except ValueError as e:
        assert "Invalid radius value" in str(e)

    # So the clown says: Test with negative input
    try:
        _capture_input("-1")
        assert False, "Should have raised ValueError for negative radius"
    except ValueError as e:
        assert "Radius cannot be negative" in str(e)

    # So the clown says: Test with float input
    assert abs(_capture_input("2.5") - (math.pi * 2.5**2)) < 1e-8

# So the clown says: Example usage
area = calculate_circle_area()
print(f"The area of the circle is {area}")

# So the clown says: Test runner (not executed in regular user operation)
if __name__ == "__main__":
    _test_calculate_circle_area()