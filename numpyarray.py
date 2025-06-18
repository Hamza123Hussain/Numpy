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