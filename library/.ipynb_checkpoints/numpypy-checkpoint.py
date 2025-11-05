import numpy as np

# reshape operation
# arr = np.array([1,2,3,4,5,6])
# reshaped = arr.reshape(2,3)
# print("Original array", arr)
# print("reshaped (2*3): \n", reshaped)


# transpose operation
# matrix = np.array([[1,2,3],
#                   [4,5,6]])
# transpose = np.transpose(matrix)
# print("Original matrix is\n",matrix)
# print("after transpose\n", transpose)



# Arithmetic Operations
# a = np.array([10, 20, 30])
# b = np.array([1, 2, 3])
# print("Addition:", a + b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", a / b)
# print("Power:", a ** 2)


# matrix operation   dot product
# A = np.array([[1, 2],
#               [3, 4]])

# B = np.array([[5, 6],
#               [7, 8]])
# result = A @ B  
# print("Matrix Multiplication:\n", result)


# Aggregation Functions
# arr = np.array([[1, 2, 3],
#                 [4, 5, 6]])

# print("Sum:", np.sum(arr))
# print("Mean:", np.mean(arr))
# print("Max:", np.max(arr))
# print("Min:", np.min(arr))
# print("Standard Deviation:", np.std(arr))
# print("Row-wise Sum:", np.sum(arr, axis=1))
# print("Column-wise Sum:", np.sum(arr, axis=0))


# Flatten Operation   Converts a multi-dimensional array into a single (1D) array.
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# flat = arr.flatten()
# print("Flattened Array:", flat)


# Concatenation  Combine (join) two or more arrays together.

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# combined = np.concatenate((a, b))
# print("Concatenated Array:", combined)

# Slicing   Extract specific portions of an array.

# arr = np.array([10, 20, 30, 40, 50, 60])
# print("First 3 elements:", arr[:3])
# print("Elements from index 2 to 4:", arr[2:5])
# print("Alternate elements:",arr[::2])

# Sorting  Sorts array elements in ascending order.
# arr = np.array([9, 3, 1, 7, 5])
# print("Sorted Array:", np.sort(arr))


# Unique Elements   Returns unique values from an array.
arr = np.array([1, 2, 2, 3, 3, 3, 4])
unique = np.unique(arr)
print("Unique Elements:", unique)
