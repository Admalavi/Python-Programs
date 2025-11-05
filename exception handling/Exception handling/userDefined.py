class AgeTooSmallError(Exception):
    pass

try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise AgeTooSmallError("Age must be 18 or above!")
    else:
        print("You are eligible!")
except AgeTooSmallError as e:
    print("Custom Exception:", e)
