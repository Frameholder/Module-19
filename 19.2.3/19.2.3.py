import pytest
from app.Calculator import Calculator

class TestCalc:
    def setup(self):
        self.Calc = Calculator

    def test_multiply_correctly(self):
        assert self.Calc.multiply(self,2,2)==4

    def test_division_correctly(self):
        assert self.Calc.division(self,2,2)==1

    def test_subtraction_correctly(self):
        assert self.Calc.subtraction(self,4,2)==2

    def test_adding_correctly(self):
        assert self.Calc.adding(self, 4, 2) == 6

