import math


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def square(x, y):
    return x ** 2
    return y ** 2

def squareROOT(x):
    return math.sqrt(x)
    
print("Select operation.")
print("1.Add (+)")
print("2.Subtract (-)")
print("3.Multiply (*)")
print("4.Divide (/)")
print("5.Square (²)")
print("6.SquareRoot (√)")
print("q to exit")

while True:
    
    choice = input("Enter choice(1/2/3/4/5/6/q): ")
    
    if choice == "q":
        break

    if choice in ('1', '2', '3', '4', '5', '6'):
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        elif choice == '5':
            print(num1, "**", 2, "=", square(num1, num1))
            print(num2, "**", 2, "=", square(num2, num2))

        elif choice == '6':
            print (math.sqrt(num1))
            
        next_calculation = input("Let's do next calculation? (yes/no): ")
        
        if next_calculation == "yes":
            print("Select operation.")
            print("1.Add")
            print("2.Subtract")
            print("3.Multiply")
            print("4.Divide")
            print("5.Square")
            print("6.SquareRoot")
            print("q to exit")
        
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
