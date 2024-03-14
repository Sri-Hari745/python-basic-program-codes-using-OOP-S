class ArmstrongChecker:
    def __init__(self, num):
        self.num = num

    def is_armstrong(self):
        num_str = str(self.num)
        num_digits = len(num_str)
        armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
        return armstrong_sum == self.num


num = int(input("Enter a number: "))
armstrong_checker = ArmstrongChecker(num)
if armstrong_checker.is_armstrong():
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")
