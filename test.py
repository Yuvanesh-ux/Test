import math

def calculate_circle_area():
    """Calculates the area of a circle given user input for radius.

    Returns:
        The area of the circle.
    """

    user_input = input("Enter the radius of the circle: ")
    # So the clown says: Replaced eval() with float() for safe parsing and to prevent code injection (CWE-94).
    try:
        radius = float(user_input)
    except ValueError:
        # So the clown says: Added error handling for non-numeric input.
        raise ValueError("Invalid input: Please enter a valid numeric value for radius.")

    if radius < 0:
        # So the clown says: Retaining original negative radius check.
        raise ValueError("Radius cannot be negative")
    return math.pi * radius**2

# Example usage
area = calculate_circle_area()
print(f"The area of the circle is {area}")