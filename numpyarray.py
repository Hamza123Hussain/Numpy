import numpy as np
# Creating a 1-dimensional NumPy array (vector)
Single_Dim_Array = np.array([1, 2, 1, 3])
# This creates an array with a single row of elements.
# Think of it like a list of numbers.
# Creating a 2-dimensional NumPy array (matrix)
Two_Dimesniona_Array = np.array([[1, 2, 2], [1, 3, 1]])
# This creates an array with rows and columns, similar to a table or spreadsheet.
# The outer brackets `[[...]]` define the entire array, and each inner bracket `[...]` represents a row.
print('Shape of One D Array', Single_Dim_Array.shape)
# The `.shape` attribute tells you the dimensions of the array.
# For a 1D array, it returns a tuple with one element: the number of elements in the array.
# In this case, `(4,)` means there are 4 elements.
print('Shape of Two D Array', Two_Dimesniona_Array.shape)
# For a 2D array, `.shape` returns a tuple `(rows, columns)`.
# Here, `(2, 3)` means there are 2 rows and 3 columns.
# Creating a multi-dimensional NumPy array (tensor)
MultiDimensionArray = np.array([[[1, 2, 3], [1, 1, 2]], [[1, 21, 22], [12, 12, 12]]])
# This is a 3-dimensional array. Imagine stacking multiple 2D arrays on top of each other.
print('Shape of Multi D Array', MultiDimensionArray.shape)
# For a 3D array, `.shape` returns a tuple `(depth, rows, columns)`.
# Here, `(2, 2, 3)` means there are 2 "layers" (or blocks), each with 2 rows and 3 columns.
print('Size of Array', Single_Dim_Array.size)
# The `.size` attribute tells you the total number of elements in the array, regardless of its shape.
# For `Single_Dim_Array` (which is `[1, 2, 1, 3]`), the size is 4.
print('Data of Array', MultiDimensionArray.dtype)
# The `.dtype` attribute tells you the data type of the elements stored in the array.
# NumPy arrays are designed to hold elements of a single, uniform data type (e.g., all integers, all floats).
# In this case, it will likely be `int32` or `int64`, indicating integers.
print('Dimensions of Array', MultiDimensionArray.ndim)
# The `.ndim` attribute tells you the number of dimensions (or axes) of the array.
# For `MultiDimensionArray`, which is a 3D array, `ndim` will be 3.
# A 1D array has `ndim = 1`, a 2D array has `ndim = 2`, and so on.

# ---------------------- np.zeros ----------------------
# ✅ Create a 1D NumPy array with 4 elements, all initialized to 0.0 (default dtype is float)
array1 = np.zeros(4)  
# Output: [0. 0. 0. 0.]
# Shape: (4,)
# ✅ Create a 2D array of shape (2 rows, 3 columns), all elements initialized to 0
# dtype=int means all values will be of integer type instead of default float
array2 = np.zeros((2, 3), dtype=int)  
# Output:
# [[0 0 0]
#  [0 0 0]]
# Shape: (2, 3)
# ---------------------- np.ones ----------------------
# ✅ Create a 1D NumPy array with 4 elements, all initialized to 1.0 (default dtype is float)
array3 = np.ones(4)
# Output: [1. 1. 1. 1.]
# Shape: (4,)
# ✅ Create a 2D array of shape (2x3), all values set to 1 and type set to integer
array4 = np.ones((2, 3), dtype=int)
# Output:
# [[1 1 1]
#  [1 1 1]]
# Shape: (2, 3)
# ---------------------- np.full ----------------------
# ✅ Create a 1D array with 4 elements, all initialized to value 5 (default dtype is inferred from value)
array5 = np.full(4, 5)
# Output: [5 5 5 5]
# Shape: (4,)
# ✅ Create a 2D array of shape (2x3), all elements initialized to 5
array6 = np.full((2, 3), 5)
# Output:
# [[5 5 5]
#  [5 5 5]]
# Shape: (2, 3)

# ---------------------- np.arange ----------------------
# ✅ Create a 1D array using np.arange
# Syntax: np.arange(start, stop, step, dtype)
# Starts from 2, stops *before* 10, with a step of 2
# Result: [2, 4, 6, 8]
array7 = np.arange(2, 10, 2, dtype=int)
# Explanation:
# Start at 2 → next is 4 → then 6 → then 8 → 10 is excluded
# dtype=int ensures all elements are integers
# Shape: (4,)
# Output: [2 4 6 8]

# ❌ Incorrect usage of np.array
# np.array expects a sequence (like a list, tuple, etc.), not multiple separate numbers
# The following line will throw a TypeError:
# array8 = np.array(2, 10, dtype=int)

# ✅ Correct way: Wrap the values in a list or tuple to create a 1D array
array8 = np.array([2, 10], dtype=int)
# Creates a 1D array with 2 elements: [2, 10]
# dtype=int specifies the data type
# Output: [ 2 10 ]

# ---------------------- np.eye ----------------------
# ✅ Create a 2D square identity matrix of shape (3x3)
# np.eye(N, dtype=int) → creates an identity matrix with N rows and N columns
# An identity matrix has 1s on the main diagonal and 0s elsewhere
array9 = np.eye(3, dtype=int)
# Output:
# [[1 0 0]
#  [0 1 0]
#  [0 0 1]]
# Shape: (3, 3)
# dtype=int ensures all values are integers
# ✅ Create a 2D identity-like matrix of shape (3x4)
# np.eye(N, M, dtype=int) → creates a matrix with N rows and M columns
# It will still place 1s on the "main diagonal" (where row index == column index), up to the smallest of N or M
array10 = np.eye(3, 4, dtype=int)
# Output:
# [[1 0 0 0]
#  [0 1 0 0]
#  [0 0 1 0]]
# Shape: (3, 4)
# dtype=int ensures the values are integers

# ---------------------- np.linspace ----------------------

# ✅ Create 5 evenly spaced numbers between 0 and 1 (inclusive)
# Syntax: np.linspace(start, stop, num)
array11 = np.linspace(0, 1, 5)
# Explanation:
# It includes both start (0) and stop (1) by default.
# Divides the interval [0, 1] into 4 equal parts (5 numbers total).
# Output: [0.   0.25 0.5  0.75 1.  ]
# dtype is float by default
# Shape: (5,)

# ✅ Create 5 evenly spaced numbers between 0 and 10, excluding the endpoint
# Syntax: np.linspace(start, stop, num, endpoint=False, dtype=int)
array12 = np.linspace(0, 10, 5, endpoint=False, dtype=int)
# Explanation:
# It excludes the stop value (10) because endpoint=False.
# It will generate 5 values spaced equally in the interval [0, 10).
# The values: [0, 2, 4, 6, 8] — equally spaced with step size = 2
# dtype=int casts the float results to integers
# Shape: (5,)
# Output: [0 2 4 6 8]

#  ---------------------- np.random.rand ----------------------

# ✅ Generate 5 random numbers between 0 and 1 (uniform distribution)
array111 = np.random.rand(5)
# Output: [0.715 0.312 ...]  (random values)
# Shape: (5,)
# Each number is drawn from a **uniform distribution** over [0, 1)
# Note: All values are floats between 0 (inclusive) and 1 (exclusive)

# ✅ Generate a 2D array (2 rows, 55 columns) of random values between 0 and 1
array211 = np.random.rand(2, 55)
# Output: 2x55 matrix with values in [0, 1)
# Shape: (2, 55)
# Again, values are from a uniform distribution

# ---------------------- np.random.randn ----------------------

# ✅ Generate 5 random numbers from the **standard normal distribution**
array311 = np.random.randn(5)
# Output: [ 1.53 -0.71 ...] (random values)
# Shape: (5,)
# Values follow a **normal distribution** with mean 0 and standard deviation 1 (μ=0, σ=1)
# Can include negative and positive numbers, unlike `rand()`

# ---------------------- np.random.normal ----------------------

# ✅ Generate a 2D array of shape (2, 3) from a **normal distribution**
# Parameters: mean=0, std=1, size=(2, 3)
array411 = np.random.normal(0, 1, (2, 3))
# Output: 2x3 matrix with normally distributed values
# Each value is drawn from N(0, 1)
# Shape: (2, 3)

# ---------------------- np.random.randint ----------------------

# ✅ Generate a 2D array of random integers from 0 (inclusive) to 10 (exclusive)
array122 = np.random.randint(0, 10, (2, 3))
# Output: 2x3 matrix of random integers like [[3 7 1], [4 0 9]]
# Values are between 0 and 9 (10 is excluded)
# Shape: (2, 3)
# dtype: int

# ---------------------- Example Array ----------------------

# Let's create a 2D NumPy array (2 rows, 3 columns)
array = np.array([[1, 2, 3], [4, 5, 6]])
# This array looks like:
# [[1 2 3]
#  [4 5 6]]

# ✅ Check the number of dimensions
print(array.ndim)
# Output: 2
# .ndim gives the number of dimensions (axes) of the array
# 2D array → .ndim = 2
# 1D array → .ndim = 1, 3D array → .ndim = 3, etc.

# ✅ Check the shape of the array
print(array.shape)
# Output: (2, 3)
# .shape returns a tuple representing the array’s shape
# (2, 3) means 2 rows and 3 columns

# ✅ Check the total number of elements
print(array.size)
# Output: 6
# .size returns the total number of elements in the array
# 2 rows × 3 columns = 6 elements

# ✅ Check the data type of elements in the array
print(array.dtype)
# Output: int64 (or int32 depending on system)
# .dtype returns the data type of the array elements
# You can also set the dtype when creating an array like:
# np.array([[1, 2], [3, 4]], dtype=float)
