"""Validate numeric inputs."""
from math import isfinite


def numeric_values(values):
    numbers = []
    for value in values:
        try:
            number = float(value)
        except (TypeError, ValueError, OverflowError):
            raise ValueError("Not numeric.")
        if not isfinite(number):
            raise ValueError("Not finite.")
        numbers.append(number)
    return tuple(numbers)
