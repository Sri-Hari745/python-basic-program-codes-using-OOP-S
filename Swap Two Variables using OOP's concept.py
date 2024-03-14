class VariableSwapper:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def swap_variables(self):
        self.var1, self.var2 = self.var2, self.var1
        return self.var1, self.var2


var1 = input("Enter the first variable: ")
var2 = input("Enter the second variable: ")
variable_swapper = VariableSwapper(var1, var2)
var1, var2 = variable_swapper.swap_variables()
print("After swapping, the first variable is:", var1)
print("After swapping, the second variable is:", var2)
