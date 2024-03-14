class Number:
    def __init__(self, num):
        self.num = num

    def is_even(self):
        return self.num % 2 == 0

    def is_odd(self):
        return not self.is_even()


num = int(input("Enter a number: "))
number_obj = Number(num)  # reference variable
if number_obj.is_even():
    print(num, "The number is even.")
else:
    print("The number is odd.")
