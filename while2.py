#check entered number is even or odd
# n = int(input("Enter a number: "))
# if n <= 1:
#     print("Not prime")
# else:
#     i = 2
#     while i < n:
#         if n % i == 0:
#             print("Not prime")
#             break
#         i += 1
#     else:
#         print("Prime")




#sum of digits of a number:
# n = int(input("enter number: "))
# sum = 0
# while n > 0:
#     digit = n % 10
#     sum += digit
#     n //= 10
# print("Sum of digits:",sum)




#palindrome number:
# num = int(input("Enter number: "))
# orig = num
# rev = 0
# while num > 0:
#     rev = rev * 10 + num % 10
#     num //= 10
# print("Palindrome" if rev == orig else "Not Palindrome")





#reverse of a number:
# num = int(input("Enter number: "))
# rev = 0
# while num > 0:
#     rev = rev * 10 + num % 10
#     num //= 10
# print("Reversed number:", rev)




# multiplication table of a number:
# num = int(input("Enter number: "))
# i = 1
# while i <= 10:
#     print(f"{num} x {i} = {num * i}")
#     i += 1



# largest of n numbers:
# n = int(input("Enter how many numbers: "))
# count = 0
# max_num = float('-inf')
# while count < n:
#     x = int(input("Enter number: "))
#     if x > max_num:
#         max_num = x
#     count += 1
# print("Largest:", max_num)




# smallest of n numbers:
# n = int(input("How many numbers do you want to enter? "))

# count = 0
# min_num = float('inf')

# while count < n:
#     x = int(input("Enter number: "))
#     if x < min_num:
#         min_num = x
#     count += 1

# print("Smallest:", min_num)
