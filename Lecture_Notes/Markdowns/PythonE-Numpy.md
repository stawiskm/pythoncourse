# **Guide to Using NumPy with Python**

---

## **Introduction to NumPy**

**NumPy** is a powerful library in Python that provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently. It is the foundation for many other scientific computing libraries like SciPy, Pandas, and more.

---

## **Installation**

To use NumPy, you need to install it. You can install NumPy using pip:

```bash
pip install numpy
```

---

## **Importing NumPy**

Once installed, you can import NumPy into your Python script or Jupyter Notebook. It is customary to import it using the alias `np`:

```python
import numpy as np
```

---

## **Basic Array Operations**

### **1. Creating Arrays**

- **From Lists:**

You can create a NumPy array from a Python list using the `np.array()` function.

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
```

- **Multi-Dimensional Arrays:**

Create 2D or multi-dimensional arrays by passing nested lists.

```python
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)
```

- **Zeros and Ones:**

Create arrays filled with zeros or ones using `np.zeros()` and `np.ones()`.

```python
zeros = np.zeros((3, 3))
ones = np.ones((2, 4))
```

- **Range and Linspace:**

Use `np.arange()` to create arrays with a specified range and step size, or `np.linspace()` to create an array of evenly spaced values.

```python
range_array = np.arange(0, 10, 2)
linspace_array = np.linspace(0, 1, 5)
```

### **2. Array Attributes**

Explore important attributes of arrays:

- **Shape:**

The shape of an array tells you its dimensions.

```python
print(matrix.shape)
```

- **Size:**

The total number of elements in the array.

```python
print(matrix.size)
```

- **Data Type:**

Check the data type of the array elements.

```python
print(arr.dtype)
```

---

## **Indexing and Slicing**

NumPy arrays can be indexed and sliced similarly to Python lists, but with more power, especially for multi-dimensional arrays.

### **1. Indexing**

- **1D Array:**

```python
arr = np.array([10, 20, 30, 40, 50])
print(arr[2])  # Outputs 30
```

- **2D Array:**

```python
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix[1, 2])  # Outputs 6
```

### **2. Slicing**

- **1D Array:**

```python
print(arr[1:4])  # Outputs [20 30 40]
```

- **2D Array:**

```python
print(matrix[:, 1])  # Outputs second column [2 5 8]
```

### **3. Fancy Indexing**

Select elements from arrays using lists or arrays of indices.

```python
arr = np.array([10, 20, 30, 40, 50])
indices = [0, 2, 4]
print(arr[indices])  # Outputs [10 30 50]
```

---

## **Array Operations**

NumPy supports element-wise operations as well as matrix operations.

### **1. Element-wise Operations**

```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Element-wise addition
print(arr1 + arr2)

# Element-wise multiplication
print(arr1 * arr2)
```

### **2. Universal Functions (ufuncs)**

NumPy provides many mathematical functions that operate element-wise.

```python
arr = np.array([1, 2, 3, 4])

# Square root
print(np.sqrt(arr))

# Exponential
print(np.exp(arr))
```

There is a wide range of ufuncs available in NumPy for various mathematical operations: `np.sin()`, `np.cos()`, `np.log()`, `np.sum()`, `np.mean()`, and more.

### **3. Matrix Operations**

- **Dot Product:**

```python
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

result = np.dot(matrix1, matrix2)
print(result)
```

- **Transpose:**

```python
print(matrix1.T)
```

---

## **Broadcasting**

Broadcasting allows NumPy to perform element-wise operations on arrays of different shapes.

```python
arr = np.array([1, 2, 3])
matrix = np.array([[10, 20, 30], [40, 50, 60]])

# Broadcasting arr to match the shape of matrix
result = matrix + arr
print(result)
```

---

## **Aggregations**

NumPy provides a variety of aggregation functions:

```python
arr = np.array([1, 2, 3, 4, 5])

# Sum
print(np.sum(arr))

# Mean
print(np.mean(arr))

# Maximum
print(np.max(arr))

# Minimum
print(np.min(arr))
```

For multi-dimensional arrays, you can specify the axis:

```python
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# Sum along the columns
print(np.sum(matrix, axis=0))

# Sum along the rows
print(np.sum(matrix, axis=1))
```

---

## **Difference and Cumulative Sum**

### **1. `np.diff`: Compute Differences Between Elements**

The `np.diff()` function calculates the difference between consecutive elements in an array.

- **1D Array:**

```python
arr = np.array([10, 20, 30, 40, 50])
diff = np.diff(arr)
print(diff)  # Outputs [10 10 10 10]
```

- **2D Array:**

For 2D arrays, you can specify the axis along which to calculate the differences.

```python
matrix = np.array([[1, 2, 4],
                   [7, 11, 13]])
diff_axis0 = np.diff(matrix, axis=0)  # Difference along rows
diff_axis1 = np.diff(matrix, axis=1)  # Difference along columns
print(diff_axis0)  # Outputs [[6 9 9]]
print(diff_axis1)  # Outputs [[ 1  2] [ 4  2]]
```

### **2. `np.cumsum`: Compute Cumulative Sum**

The `np.cumsum()` function returns the cumulative sum of elements along a given axis.

- **1D Array:**

```python
arr = np.array([1, 2, 3, 4, 5])
cumsum = np.cumsum(arr)
print(cumsum)  # Outputs [ 1  3  6 10 15]
```

- **2D Array:**

For 2D arrays, you can also specify the axis.

```python
matrix = np.array([[1, 2, 3], [4, 5, 6]])
cumsum_axis0 = np.cumsum(matrix, axis=0)  # Cumulative sum along columns
cumsum_axis1 = np.cumsum(matrix, axis=1)  # Cumulative sum along rows
print(cumsum_axis0)  # Outputs [[ 1  2  3] [ 5  7  9]]
print(cumsum_axis1)  # Outputs [[ 1  3  6] [ 4  9 15]]
```

---

## **Reshaping and Resizing**

- **Reshape:**

Change the shape of an array without changing its data.

```python
arr = np.arange(1, 7)
reshaped = arr.reshape((2, 3))
print(reshaped)
```

- **Flatten:**

Convert a multi-dimensional array to a 1D array.

```python
flattened = reshaped.flatten()
print(flattened)
```

---

## **Random Numbers**

NumPy's `random` module provides functions for generating random numbers.

```python
# Random integers
rand_ints = np.random.randint(0, 10, size=(3, 3))

# Random floats between 0 and 1
rand_floats = np.random.rand(3, 3)

# Normal distribution
rand_normal = np.random.randn(3, 3)
```

---

## **Saving and Loading Data**

- **Save:**

You can save arrays to disk in binary format using `np.save()` or in text format using `np.savetxt()`.

```python
np.save('array.npy', arr)
np.savetxt('array.txt', arr)
```

- **Load:**

Load arrays from files.

```python
loaded_arr = np.load('array.npy')
loaded_txt_arr = np.loadtxt('array.txt')
```

---

## **Practice Problems**

1. Create a 4x4 matrix with values ranging from 0 to 15.
2. Create a 3x3 identity matrix.
3. Generate a 10x10 matrix with random values and find the minimum and maximum values.
4. Subtract the mean of each row of a given matrix.
5. Multiply two matrices of size 3x3 and 3x2.
6. Find the difference between consecutive elements of a 1D array.
7

. Compute the cumulative sum of a 2D matrix along both axes.

---

## **Conclusion**

NumPy is a vast library with capabilities far beyond what is covered in this guide. This introduction should help you get started with basic array operations, mathematical functions, and array manipulation. As you progress, you'll find that NumPy is indispensable for scientific computing and data analysis in Python. Happy coding!
