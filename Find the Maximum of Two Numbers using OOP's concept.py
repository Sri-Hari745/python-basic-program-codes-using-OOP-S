class MaximumFinder:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def find_maximum(self):
        return max(self.num1, self.num2)


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
maximum_finder = MaximumFinder(num1, num2)
print("The maximum of the two numbers is:", maximum_finder.find_maximum())
