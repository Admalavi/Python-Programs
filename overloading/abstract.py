# from abc import ABC, abstractmethod

# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class rect(shape):
#     def area(self,l,b):
#         self.l=l
#         self.b=b
#         return 2*l*b   

# r=rect()     
# print(r.area(10,5))






from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class rect(shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print("area is: ",2*self.l*self.b)

r=rect(10,5)     
r.area()