class Factorial:
    def __init__(self, num):
        self.num = num

    def calculate_factorial(self):
        return (lambda f: f(f))(lambda f: (lambda x: 1 if x == 0 else x * f(f)(x - 1)))(self.num)


num = int(input("Enter a number: "))
factorial_calculator = Factorial(num)
print("The factorial of the number is:", factorial_calculator.calculate_factorial())
