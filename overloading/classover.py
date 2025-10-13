class emp:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal

class fun(emp):
    def __init__(self,name,sal,age):
        super().__init__(name,sal)
        self.age=age

e=fun("akshata",50000,21)
print(e.name,e.sal,e.age)

