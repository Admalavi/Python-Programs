try:
    a = int(input("Enter value for a"))
    b = int(input("Enter value for b"))
    print(a / b)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")

print("Program continues...")
