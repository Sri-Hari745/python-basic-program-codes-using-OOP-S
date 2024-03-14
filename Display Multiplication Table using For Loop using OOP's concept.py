class MultiplicationTable:
    def __init__(self, num):
        self.num = num

    def display_table(self):
        for i in range(1, 11):
            print(f"{self.num} x {i} = {self.num * i}")


num = int(input("Enter a number to display its multiplication table: "))
multiplication_table = MultiplicationTable(num)
multiplication_table.display_table()
