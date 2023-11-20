import random as rd
import math


def random_points(radius, x_center, y_center):
    x = x_center + radius + 1
    y = y_center + radius + 1
    while math.sqrt((x_center - x) ** 2 + (y_center - y) ** 2) > radius:
        x = rd.uniform(x_center - radius, x_center + radius)
        y = rd.uniform(y_center - radius, y_center + radius)
    return x, y
