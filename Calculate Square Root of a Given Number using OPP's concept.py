import math


class SquareRootCalculator:
    def __init__(self, num):
        self.num = num

    def calculate_square_root(self):
        return math.sqrt(self.num)


num = float(input("Enter a number: "))
square_root_calculator = SquareRootCalculator(num)
print("The square root of the number is:", square_root_calculator.calculate_square_root())
