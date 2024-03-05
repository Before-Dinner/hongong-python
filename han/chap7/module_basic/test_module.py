import math

PI = math.pi

def number_input() -> float:
    radius = float(input("> "))
    return radius 

def get_circle_circumference(radius: float) -> float:
    return 2 * PI * radius

def get_circle_area(radius: float) -> float:
    return pow(radius, 2) * PI

