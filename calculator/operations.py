"""Static calculator operations."""
from math import sqrt, pow


class Operations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b

    @staticmethod
    def square(value):
        return value * value

    @staticmethod
    def sqrt(value):
        return sqrt(value)

    @staticmethod
    def sum(*values):
        if not values:
            raise ValueError("Values required.")
        return sum(values)

    @staticmethod
    def power(value, *, exponent=2):
        return pow(value, exponent)
