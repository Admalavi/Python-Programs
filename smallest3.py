a =int(input("enter value of a :"))
b =int(input("enter value of b: "))
c =int(input("enter value of c: "))

print(a)
print(b)
print(c)

if a < b and a < c:
    print("a is smaller")
elif b < a and b < c:
    print("b is smaller") 
else:
    print("c is smaller")       