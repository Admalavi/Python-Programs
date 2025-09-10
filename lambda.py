# #function
# def fun():
#     print("hello akshata")
# fun()   


# #function with parameters
# def add(a,b):
#     print(a+b)
# add(10,26)    



# def evenodd():
#     num = int(input("enter a number: "))
#     if(num % 2 == 0):
#         print("even")
#     else:
#         print("odd")
# evenodd()    






# #lambda functions
# square = lambda x: x * x
# print(square(4))

# add =lambda a,b: a+b
# print(add(10,26))

# ex = lambda k,m:k**m
# print(ex(2,3))




# #array module in python
# import array as arr
# num = arr.array('i',[10,20,30,40,50])
# print(num)
# print(num[1])
# print(num[1:3])
# print(num.insert(2,26))
# print(num)
# print(num.count(10))
# print(num.reverse())
# print(num)


#array using for loop
import array as arr
num = arr.array('i',[1,2,3])
for i in num:
    print(i)


#array with float values
b = arr.array('d', [2.5, 3.2, 3.3])
print(b[1])
print(b[2])


#slicing of array
import array as arr
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = arr.array('i', a)

res = a[3:8]
print(res)

res =a[8:]
print(res)

res = a[:4]
print(res)

res=a[1:9:2]
print(res)