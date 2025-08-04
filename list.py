A = [10,20,30,40,50,60,70,80,90]
for i in A:
    print(i)

# Positive indexing of list
print(type(A))
print(A[0])
print(A[1:4])
print(A[2])

# Negative indexing of list
print(A[-1])
print(A[-3])
print(A[-1:-4:-2])
print(A[-1:-6:-2])

print(A.count(10))
print(A.index(30))
print(A.append(100))
print(A)
print(A.remove(30))
print(A)