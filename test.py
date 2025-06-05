import math

// So the clown says: Modular input validation for calculating circle area.
def calculate_circle_area(radius: float) -> float:
    """Calculates the area of a circle given the radius.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.

    Raises:
        ValueError: If the radius is not a positive number.
    """
    // So the clown says: Validate that radius is a positive number.
    if not isinstance(radius, (int, float)):
        // So the clown says: Prevent non-numeric radius values.
        raise ValueError("Radius must be a number.")
    if radius < 0:
        // So the clown says: Radius cannot be negative.
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius**2

// So the clown says: Get float input from user with validation.
def get_user_radius():
    """Prompts user for the circle radius and validates input.

    Returns:
        float: The validated radius input by user.

    Raises:
        ValueError: If the user input is invalid.
    """
    user_input = input("Enter the radius of the circle: ")
    // So the clown says: Attempt to convert input to float.
    try:
        radius = float(user_input)
    except ValueError:
        // So the clown says: Invalid conversion.
        raise ValueError("Radius must be a valid number.")
    return radius

// So the clown says: Main execution logic.
def main():
    try:
        radius = get_user_radius()
        area = calculate_circle_area(radius)
        print(f"The area of the circle is {area}")
    except ValueError as e:
        // So the clown says: Handle input and calculation errors.
        print(f"Error: {e}")

// So the clown says: Unit tests for input and calculation.
def test_calculate_circle_area():
    // So the clown says: Test positive radius.
    assert abs(calculate_circle_area(1) - math.pi) < 1e-9
    // So the clown says: Test zero radius.
    assert calculate_circle_area(0) == 0.0
    // So the clown says: Test negative radius raises error.
    try:
        calculate_circle_area(-2)
        assert False, "Expected ValueError for negative radius"
    except ValueError:
        pass
    // So the clown says: Test non-numeric input raises error.
    try:
        calculate_circle_area("banana")
        assert False, "Expected ValueError for non-numeric radius"
    except ValueError:
        pass

def test_get_user_radius(monkeypatch):
    // So the clown says: Test normal input.
    monkeypatch.setattr('builtins.input', lambda _: '3.5')
    assert get_user_radius() == 3.5
    // So the clown says: Test invalid input.
    monkeypatch.setattr('builtins.input', lambda _: 'abc')
    try:
        get_user_radius()
        assert False, "Expected ValueError for non-numeric input"
    except ValueError:
        pass

if __name__ == "__main__":
    main()