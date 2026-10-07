from calculator.factory import CalculationFactory


addition = CalculationFactory.create(
    "add", 2, 3
)

power = CalculationFactory.create(
    "power",
    3,
    exponent=4
)

print(addition.get_result())
print(power.get_result())
