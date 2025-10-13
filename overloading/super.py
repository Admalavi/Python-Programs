class parent:
    def show(self):
        print("parent class")

class child(parent):
    def show(self):
        super().show()   #call parent class show method
        print("child class")
c=child()
c.show()        
