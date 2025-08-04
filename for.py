#print numbers from 1 to n:
# n = int(input("Enter n: "))
# for i in range(1, n+1):
#     print(i, end=' ')



# print even numbers from 1 to n:
# n = int(input("Enter n: "))
# for i in range(2, n+1, 2):
#     print(i, end=' ')



# print odd numbers from 1 to n:
# n = int(input("Enter n: "))
# for i in range(1, n+1, 2):
#     print(i, end=' ')




#print 1 2 4 8 16 ... until n^2:
# n = int(input("Enter n: "))
# val = 1
# while val <= n**2:
#     print(val, end=' ')
#     val *= 2



#sum of sequence 1 + 1/2! + 1/3! + ... + 1/n!:
# n = int(input("Enter n: "))
# import math
# sum_seq = 0
# for i in range(n+1):
#     sum_seq += 1 / math.factorial(i)
# print("\nSum:", sum_seq)





# Calculate cos(x) using :
import math
x = float(input("Enter x (in radians): "))
n_terms = int(input("Enter number of terms: "))
cos_x = 0
for i in range(n_terms):
    cos_x += ((-1)**i) * (x**(2*i)) / math.factorial(2*i)
print("cos(x):", cos_x)




# Check if square root of a number is prime:
# import math
# num = int(input("Enter number: "))
# sqrt_num = int(math.sqrt(num))
# if sqrt_num * sqrt_num != num:
#     print("Square root is not an integer.")
# else:
#     is_prime = True
#     for i in range(2, int(sqrt_num**0.5)+1):
#         if sqrt_num % i == 0:
#             is_prime = False
#             break
#     print("Prime" if is_prime and sqrt_num > 1 else "Not prime")






# 8. Print ABC pattern (3 rows)
# for _ in range(3):
#     for ch in range(ord('A'), ord('D')):
#         print(chr(ch), end=' ')
#     print()




# 9. Increasing ABC pattern
# n = int(input("enter n: "))
# for i in range(1, n+1):
#     for ch in range(ord('A'), ord('A') + i):
#         print(chr(ch), end=' ')
#     print()




# 10. Decreasing ABC pattern
# n = int(input("enter n: "))
# for i in range(n, 0, -1):
#     for ch in range(ord('A'), ord('A') + i):
#         print(chr(ch), end=' ')
#     print()





# 11. Increasing number triangle
# n = int(input("enter n: "))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end=' ')
#     print()




# 12. Repeating number pattern
# n = int(input("enter n: "))
# for i in range(1, n+1):
#     for j in range(i):
#         print(i, end=' ')
#     print()
