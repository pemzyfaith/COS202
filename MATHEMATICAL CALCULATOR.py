print("MATHEMATICAL CALCULATOR")

while True:
    choice = input("\nEnter (+, -, *, /, \\, %, ^, C, OFF): ").upper()

    if choice == "OFF":
        print("Calculator Off")
        quit()

    elif choice == "C":
        print("Screen Cleared")

    elif choice == "+":
        a = float(input("First Number: "))
        b = float(input("Second Number: "))
        print("Answer =", a + b)

    elif choice == "-":
        a = float(input("First Number: "))
        b = float(input("Second Number: "))
        print("Answer =", a - b)

    elif choice == "*":
        a = float(input("First Number: "))
        b = float(input("Second Number: "))
        print("Answer =", a * b)

    elif choice == "/":
        a = float(input("First Number: "))
        b = float(input("Second Number: "))
        if b == 0:
            print("Cannot divide by zero")
        else:
            print("Answer =", a / b)

    elif choice == "\\":
        a = float(input("First Number: "))
        b = float(input("Second Number: "))
        if b == 0:
            print("Cannot divide by zero")
        else:
            print("Answer =", a // b)

    elif choice == "%":
        a = float(input("First Number: "))
        b = float(input("Second Number: "))
        if b == 0:
            print("Cannot divide by zero")
        else:
            print("Answer =", a % b)

    elif choice == "^":
        a = float(input("First Number: "))
        b = float(input("Second Number: "))
        print("Answer =", a ** b)

    else:
        print("Invalid Operation")