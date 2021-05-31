import numbers


class CalculatorError(Exception):
    """An exception class for Calculator."""


class Calculator:

    def my_add(self, a, b):
        self._check_operand(a)
        self._check_operand(b)
        return a + b

    def my_subtract(self, a, b):
        return a - b

    def my_multiply(self, a, b):
        return a * b

    def my_divide(self, a, b):
        return a / b

    def _check_operand(self, operand):
        if not isinstance(operand, numbers.Number):
            raise CalculatorError(f'"{operand}" is not a number')
