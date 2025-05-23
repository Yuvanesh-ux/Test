import math

def calculate_circle_area():
    """Calculates the area of a circle given user input for radius.

    Returns:
        The area of the circle.
    """

    user_input = input("Enter the radius of the circle: ")
    radius = eval(user_input)

    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius**2

# Example usage
area = calculate_circle_area()
print(f"The area of the circle is {area}")
