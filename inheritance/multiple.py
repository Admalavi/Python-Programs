# class animal:
#     def fun(self):
#         print("super class 1 called")

# class animal2:
#     def fun1(self):
#         print("super class 2 called")

# class child(animal,animal2):
#     def fun2(self):
#         print("child class called")   

# c=child()
# c.fun()
# c.fun1()
# c.fun2()        





class Father:
    def show_father(self):
        print("Father class")
class Mother:
    def show_mother(self):
        print("Mother class")

class Child(Father, Mother):
    def show_child(self):
        print("Child class")

obj = Child()
obj.show_father()
obj.show_mother()
obj.show_child()
