class PrimeChecker:
    def __init__(self, num):
        self.num = num

    def is_prime(self):
        if self.num <= 1:
            return False
        for i in range(2, int(self.num ** 0.5) + 1):
            if self.num % i == 0:
                return False
        return True


num = int(input("Enter a number: "))
prime_checker = PrimeChecker(num)
if prime_checker.is_prime():
    print("The number is prime.")
else:
    print("The number is not prime.")
