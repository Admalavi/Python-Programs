class grandparent:
    def fun(self):
        print("grantparent class called")

class parent(grandparent):
    def fun1(self):
        print("parent class called")

class child(parent):
    def fun2(self):
        print("child class called")

s1=child()
s1.fun()
s1.fun1()
s1.fun2()        
