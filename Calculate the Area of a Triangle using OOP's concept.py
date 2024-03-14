class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
triangle = Triangle(base, height)
print("The area of the triangle is:", triangle.calculate_area())
