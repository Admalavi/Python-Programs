class math:
    def add(self,a,b):
        return a+b
    
    def add(self,a,b,c):
        return a+b+c
a=math()
# add=a.add(2,3)
# print (add)   #it will show error because 3rd parameter is missing
add=a.add(2,3,4)
print(add)






class math:
    def add(self,a=0,b=0,c=0):
        return a+b+c
a=math()
print(a.add(2))
print(a.add(2,3))
print(a.add(2,3,4))
