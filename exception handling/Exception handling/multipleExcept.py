try:
    a = int(input("Enter value for a"))
    b = int(input("Enter value for b"))
    print(a/b)
except ZeroDivisionError:
    print("you cannot divide by zero")

except ValueError:
    print("Invlide input please enter a number")
