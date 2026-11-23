#Calculator.py
print("Hello and welcome to the Calculator!")
#Input
Type = input("Enter the type of math (+, -, *, /): ").strip()
#If|Elif|Else
if Type == "+":
    Num1 = int(input("Enter the first number: "))
    Num2 = int(input("Enter the second number: "))
    Sum = Num1 + Num2
    print(f"{Num1} + {Num2} = {Sum}")
elif Type == "-":
     Num1 = int(input("Enter the first number: "))
     Num2 = int(input("Enter the second number: "))
     Difference = Num1 - Num2
     print(f"{Num1} - {Num2} = {Difference}")
elif Type == "*":
    Holdup = input("Are you going below 0 (negative) or above 0 (positive)? Choose N or P: ").strip().upper()
    if Holdup == "N":
        Num1 = float(input("Enter the first number: "))
        Num2 = float(input("Enter the second number: "))
        Product = Num1 * Num2
        print(f"{Num1} x {Num2} = {Product}")
    elif Holdup == "P":
        Num1 = int(input("Enter the first number: "))
        Num2 = int(input("Enter the second number: "))
        Product = Num1 * Num2
        print(f"{Num1} x {Num2} = {Product}")
    else:
        print("Invallid input!")
elif Type == "/":
    Holdup = input("Are you going to divide by equal or odd? Choose E or O: ").strip().upper()

    if Holdup == "E":
        Num1 = int(input("Enter the first number: "))
        Num2 = int(input("Enter the second number: "))
        Quotient = Num1 // Num2
        print(f"{Num1} / {Num2} = {Quotient}")
    elif Holdup == "O":
        Num1 = float(input("Enter the first number: "))
        Num2 = float(input("Enter the second number: "))
        Quotient = Num1 / Num2
        print(f"{Num1} / {Num2} = {Quotient}")
else:
    print("Invallid input!")