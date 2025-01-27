import numpy as np
import math
from scipy import stats
multiply = []
addition = []
subtraction = []
divide = []
while True:
    print("1. Basic Calculator", 
          "2. Trigonometric Calculator", 
          "3. Linear Equations Calculator [2 Variable]",
          "4. Exit",
          sep="\n")
    
    x = int(input("Enter the function you want to perform: "))
    

    if x == 1:
        print("You selected Basic Calculator")
        print("1. Add", "2. Subtract", "3. Multiply", "4. Divide", sep="\n")

        a = int(input("Enter the operation you want to perform: "))

        b = int(input("Enter the number of integers you want to operate on: "))
        numbers = [int(input(f"Enter number {i+1}: ")) for i in range(b)]

        if a == 1:  
            print("Addition of numbers is:", sum(numbers))
        elif a == 2:  
            difference = numbers[0]
            for num in numbers[1:]:
                difference -= num
            print("Subtraction of numbers is:", difference)
        elif a == 3:  
            print("Product of numbers is:", math.prod(numbers))
        elif a == 4:  
            try:
                result = numbers[0]
                for num in numbers[1:]:
                    result /= num
                print("Division of numbers is:", result)
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid operation selected.")
        
    elif x == 2:
        print("You selected Trigonometric Calculator")
        print("1. Sin(x)", "2. Cos(x)", "3. Tan(x)", sep="\n")
        c = int(input("Enter the operation you want to perform: "))      
        a = int(input("Enter angle: "))
        b = math.radians(a)

        if c == 1:
                print(math.sin(b))
        elif c == 2:
            print(math.cos(b))
        elif c == 3:
            print(math.tan(b))
        else:
            print("Invalid operator")
    elif x == 3:
        print("You selected Linear Equation in 2 variable Calculator")
        print("To solve linear equations, you must enter 2 equations","the equation must be in the form of ax1+bx2+C","You must enter the coefficient and constant values as asked for accurate answer", sep = "\n")
        a1 = int(input("Enter the value of a1: "))
        a2 = int(input("Enter the value of a2: "))
        b1 = int(input("Enter the value of b1: "))
        b2 = int(input("Enter the value of b2: "))
        c1 = int(input("Enter the value of c1: "))
        c2 = int(input("Enter the value of c2: "))

        A = np.array([[a1, a2],
                  [b1, b2]])
    
        B = np.array([c1, c2])
    
        try:
            solution = np.linalg.solve(A, B)
            print("\nSolutions:")
            print(f"x1 = {solution[0]}")
            print(f"x2 = {solution[1]}")
        except np.linalg.LinAlgError:
            print("Invalid equation, roots not found")

    elif x == 4:
        break
        
    else:
        print("Invalid choice! Please select a number between 1 and 4.")


