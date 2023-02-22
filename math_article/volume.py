import math


def volume_of_sphere(radius):
    volume_sphere = (4 * math.pi * radius * radius * radius) / 3
    return volume_sphere


def volume_of_cylinder(radius, height):
    volume_cylinder = math.pi * (radius * radius) * height
    return volume_cylinder


def volume_of_cone(radius, height):
    volume_cone = (math.pi * (radius * radius) * height) / 3
    return volume_cone


def volume_of_hemisphere(radius):
    volume_hemisphere = (2 * math.pi * radius * radius * radius) / 3
    return volume_hemisphere
