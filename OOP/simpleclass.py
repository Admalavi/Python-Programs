class student:
    def __init__(self, name,roll):
        self.name = name
        self.roll = roll

    def display(self):
        print("name:",self.name)
        print("roll no:",self.roll)

name = input("enter student name: ")
roll = int(input("enter roll number: "))

s1 = student(name,roll)
s1.display()