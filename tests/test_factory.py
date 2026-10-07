import pytest
from calculator.factory import CalculationFactory


def test_factory_add():
    calculation = CalculationFactory.create("add", 2, 3)
    assert calculation.get_result() == 5.0


def test_factory_normalizes_name():
    calculation = CalculationFactory.create(" ADD ", 2, 3)
    assert calculation.get_result() == 5.0


def test_factory_operations():
    assert CalculationFactory.create(
        "subtract", 5, 2
    ).get_result() == 3.0

    assert CalculationFactory.create(
        "multiply", 5, 2
    ).get_result() == 10.0

    assert CalculationFactory.create(
        "divide", 10, 2
    ).get_result() == 5.0


def test_unknown_operation():
    with pytest.raises(ValueError):
        CalculationFactory.create("bad", 2, 3)


def test_factory_does_not_execute():
    calculation = CalculationFactory.create("divide", 1, 0)

    with pytest.raises(ZeroDivisionError):
        calculation.get_result()
