import math

def calculate_circle_area(radius):
  """Calculates the area of a circle given its radius.

  Args:
    radius: The radius of the circle.

  Returns:
    The area of the circle.
  """

  if radius < 0:
    raise ValueError("Radius cannot be negative")
  return math.pi * radius**2

# Example usage
radius = 5
area = calculate_circle_area(radius)
print(f"The area of a circle with radius {radius} is {area}")
