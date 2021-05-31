
from calculator import Calculator, CalculatorError
import pytest


def test_add_weird_stuff():
    calculator = Calculator()

    with pytest.raises(CalculatorError):
        result = calculator.my_add('two', 3)


def test_add_weirder_stuff():
    calculator = Calculator()

    with pytest.raises(CalculatorError):
        result = calculator.my_add('two', 'three')


def test_add():
    calculator = Calculator()
    result = calculator.my_add(2, 3)
    assert result == 5


def test_subtract():
    calculator = Calculator()
    result = calculator.my_subtract(2, 3)
    assert result == -1


def test_multiply():
    calculator = Calculator()
    result = calculator.my_multiply(2, 3)
    assert result == 6


def test_divide():
    calculator = Calculator()
    result = calculator.my_divide(6, 3)
    assert result == 2
