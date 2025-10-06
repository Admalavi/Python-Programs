class animal:
    def name(self):
        print("name of the animal")

class dog(animal):
    def fun(self):
        print("dog")    

class cat(animal):
    def name(self):
        print("cat")  


class bat(dog,cat):
    def abc(self):
        print("bat")       


c=bat()
c.fun()
c.name()
c.abc()                  