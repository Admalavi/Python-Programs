try:
    a = int(input("Enter a number for a"))
    b = int(input("Enter number for b"))
    result = (a/b)
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result is :", result)
finally:
    print("Exception completed")
