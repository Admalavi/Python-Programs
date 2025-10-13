class animal:
    def sound(self):
        return "animal sounds"
class dog(animal):
    def sound(self):
        return "bark"
d=dog()
print(d.sound())     #sound of child class will override sound of parent class   