"""Create calculations by operation name."""
from calculator.calculation import Calculation
from calculator.operations import Operations


class CalculationFactory:
    operations = {
        "add": Operations.add,
        "subtract": Operations.subtract,
        "multiply": Operations.multiply,
        "divide": Operations.divide,
        "square": Operations.square,
        "sqrt": Operations.sqrt,
        "sum": Operations.sum,
        "power": Operations.power,
    }

    counts = {
        "add": 2,
        "subtract": 2,
        "multiply": 2,
        "divide": 2,
        "square": 1,
        "sqrt": 1,
        "power": 1,
    }

    @staticmethod
    def create(name, *values, **options):
        name = name.strip().lower()

        try:
            operation = CalculationFactory.operations[name]
        except KeyError:
            raise ValueError("Unknown operation.")

        if name in CalculationFactory.counts:
            expected = CalculationFactory.counts[name]
            if len(values) != expected:
                raise ValueError("Wrong operand count.")

        if name == "sum" and len(values) < 1:
            raise ValueError("Values required.")

        if name == "power":
            allowed = {"exponent"}
        else:
            allowed = set()

        if set(options) - allowed:
            raise ValueError("Unknown option.")

        if "exponent" in options:
            try:
                options["exponent"] = float(
                    options["exponent"]
                )
            except (TypeError, ValueError, OverflowError):
                raise ValueError("Invalid option.")

        return Calculation(
            values,
            operation,
            **options
        )
