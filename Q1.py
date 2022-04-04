#Defines a class called calculator
class Calculator:
    
    #Instantiate the two inputs
    def __init__(self, firstInput, secondInput):
        self.firstInput = firstInput
        self.secondInput = secondInput

    #Adds the two values
    def adder(self):
        result = self.firstInput + self.secondInput
        return result

    #Subtracts the two values
    def subtractor(self):
        result = self.firstInput - self.secondInput
        return result

    #Multiplies the two values
    def multiplier(self):
        result = self.firstInput * self.secondInput
        return result

    #Divides the two values
    def divider(self):
        result = self.firstInput / self.secondInput
        return result

    #Sets the two values back to 0
    def clear(self):
        self.firstInput = 0 
        self.secondInput = 0

#Obtains the two inputs for calculations
firstInput = int(input("Please enter the first number: "))
secondInput = int(input("Please enter the second number: "))

print("\n")

#Instantiates an instance of the Calculator class
calc = Calculator(firstInput, secondInput)

#Adds the inputs
add_result = calc.adder()
print("Adding " + str(calc.firstInput) + " and " + str(calc.secondInput) + " will give: " + str(add_result))

print("\n")

#Subracts the inputs
subtract_result = calc.subtractor()
print("Subtracting " + str(calc.secondInput) + " from " + str(calc.firstInput) + " will give: " + str(subtract_result))

print("\n")

#Multiplies the inputs
multiply_result = calc.multiplier()
print("Multiplying " + str(calc.firstInput) + " and " + str(calc.secondInput) + " will give: " + str(multiply_result))

print("\n")

#Divides the inputs
divide_result = calc.divider()
print("Dividing " + str(calc.firstInput) + " and " + str(calc.secondInput) + " will give: " + str(divide_result))

print("\n")

#Clears the inputs
clear_result = calc.clear()
print("The value of the first input after clear() is used is: " + str(calc.firstInput))
print("The value of the second input after clear() is used is:  " + str(calc.secondInput))