class parent:
    def fun(self):
        print("parent class")

class child1(parent):
    def fun1(self):
        print("child1 class")
class child2(parent):
    def fun2(self):
        print("child2 class")
c=child1()
c.fun()
c.fun1()
s=child2()
s.fun()   
s.fun2()                     