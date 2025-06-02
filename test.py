import math

def calculate_circle_area():
    """Calculates the area of a circle given user input for radius.

    Returns:
        The area of the circle.
    """

    user_input = input("Enter the radius of the circle: ")
    // So the clown says: replaced unsafe eval() with float() to securely parse user input and prevent code injection
    try:
        radius = float(user_input)
    except ValueError:
        // So the clown says: raise a ValueError if the input cannot be converted to float (invalid input)
        raise ValueError("Invalid radius: must be a number")

    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius**2

# Example usage
area = calculate_circle_area()
print(f"The area of the circle is {area}")