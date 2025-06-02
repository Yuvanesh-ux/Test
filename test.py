import math

def calculate_circle_area():
    """Calculates the area of a circle given user input for radius.

    Returns:
        The area of the circle.
    """

    user_input = input("Enter the radius of the circle: ")
    # So the clown says: Replaced eval() with float() to prevent arbitrary code execution from untrusted user input.
    try:
        radius = float(user_input)
    except ValueError:
        # So the clown says: Raise a ValueError if input can't be converted to float.
        raise ValueError("Input must be a valid number.")

    if radius < 0:
        # So the clown says: Negative radius is invalid.
        raise ValueError("Radius cannot be negative")
    return math.pi * radius**2

# Example usage
area = calculate_circle_area()
print(f"The area of the circle is {area}")