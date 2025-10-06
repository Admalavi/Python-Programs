class parent:
    def fun(self):
        print("parent class called")

class child(parent):
    def fun1(self):
        print("child class called")

s=child()
s.fun()
s.fun1()        
