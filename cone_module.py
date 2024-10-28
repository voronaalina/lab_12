import math

def cone_volume(radius, height):
    volume = (1/3) * math.pi * radius**2 * height
    return volume

def surface_area(radius, height):
    slant_height = math.sqrt(radius**2 + height**2)
    surf_area = math.pi * radius * (radius + slant_height)
    return surf_area
