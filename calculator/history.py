"""History storage."""
from calculator.calculation import Calculation


class History:
    def __init__(self):
        self._entries = []

    def add(self, calculation, result):
        if not isinstance(calculation, Calculation):
            raise TypeError("Invalid calculation.")
        self._entries.append((calculation, result))

    def get_history(self):
        return self._entries.copy()

    def clear(self):
        self._entries.clear()
