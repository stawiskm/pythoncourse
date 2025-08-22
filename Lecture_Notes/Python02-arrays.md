# Introduction to Python Arrays and Multidimensional Arrays

## Overview

[Video: Introduction to Python Arrays and Multidimensional Arrays](Python02-arrays_An_Introduction_to_Python_Arrays__From_Lists_to_Light_Speed.mp4)

In this guide, we will cover the basics of working with arrays and multidimensional arrays in Python. Python provides multiple ways to handle arrays, including the built-in `list` type and the `array` and `numpy` modules for more advanced usage. We will explore how to create, manipulate, and perform operations on these arrays.

## Official Documentation
- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)
- [Python Arrays](https://docs.python.org/3/library/array.html)
- [NumPy Arrays](https://numpy.org/doc/stable/user/absolute_beginners.html)

### Table of Contents

- [Introduction to Python Arrays and Multidimensional Arrays](#introduction-to-python-arrays-and-multidimensional-arrays)
  - [Overview](#overview)
    - [Table of Contents](#table-of-contents)
  - [1. Introduction to Arrays](#1-introduction-to-arrays)
    - [Lists](#lists)
    - [Arrays from the `array` module](#arrays-from-the-array-module)
  - [2. Introduction to Multidimensional Arrays](#2-introduction-to-multidimensional-arrays)
    - [Lists of Lists](#lists-of-lists)
    - [Numpy Arrays](#numpy-arrays)
  - [3. Operations on Arrays](#3-operations-on-arrays)
    - [Indexing and Slicing](#indexing-and-slicing)
      - [Lists](#lists-1)
      - [Numpy Arrays](#numpy-arrays-1)
    - [Adding, Removing, and Modifying Elements](#adding-removing-and-modifying-elements)
      - [Lists](#lists-2)
      - [Numpy Arrays](#numpy-arrays-2)
  - [4. Operations on Multidimensional Arrays](#4-operations-on-multidimensional-arrays)
    - [Indexing and Slicing](#indexing-and-slicing-1)
    - [Adding, Removing, and Modifying Elements](#adding-removing-and-modifying-elements-1)
  - [5. Common Array Functions and Methods](#5-common-array-functions-and-methods)
    - [List Methods](#list-methods)
    - [Numpy Array Functions](#numpy-array-functions)
  - [6. Excurse: Images](#6-excurse-images)
    - [Images as Arrays](#images-as-arrays)
    - [Image Processing with Numpy](#image-processing-with-numpy)
    - [Displaying Images](#displaying-images)
  - [Introduction to NumPy Arrays and Vectorized Operations](#introduction-to-numpy-arrays-and-vectorized-operations)
    - [Example 1: Using Nested For Loops](#example-1-using-nested-for-loops)
    - [Example 2: Using Array Calculations (Vectorized Operations)](#example-2-using-array-calculations-vectorized-operations)
    - [Explanation](#explanation)
    - [Output](#output)

## 1. Introduction to Arrays

### Lists

The simplest way to create an array in Python is by using a list. Lists are dynamic arrays that can hold elements of different types.

```python
# Creating a list
my_list = [1, 2, 3, 4, 5]
print(my_list)  # Output: [1, 2, 3, 4, 5]
```

### Arrays from the `array` module

For more specialized array handling, Python provides the `array` module. Arrays from this module are more memory-efficient than lists.

```python
import array

# Creating an array of integers
my_array = array.array('i', [1, 2, 3, 4, 5])
print(my_array)  # Output: array('i', [1, 2, 3, 4, 5])
```

## 2. Introduction to Multidimensional Arrays

### Lists of Lists

You can create a 2D array using lists of lists.

```python
# Creating a 2D list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
# Output:
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]
```

### Numpy Arrays

For more efficient handling of multidimensional arrays, we use the `numpy` library.

```python
import numpy as np

# Creating a 2D numpy array
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(matrix)
# Output:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
```

## 3. Operations on Arrays

### Indexing and Slicing

#### Lists

```python
# Accessing elements in a list
print(my_list[0])  # Output: 1
print(my_list[-1])  # Output: 5

# Slicing a list
print(my_list[1:3])  # Output: [2, 3]
```

#### Numpy Arrays

```python
# Accessing elements in a numpy array
print(matrix[0, 0])  # Output: 1
print(matrix[1, -1])  # Output: 6

# Slicing a numpy array
print(matrix[:, 1])  # Output: [2 5 8]
```

### Adding, Removing, and Modifying Elements

#### Lists

```python
# Adding elements
my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Removing elements
my_list.remove(2)
print(my_list)  # Output: [1, 3, 4, 5, 6]

# Modifying elements
my_list[0] = 10
print(my_list)  # Output: [10, 3, 4, 5, 6]
```

#### Numpy Arrays

```python
# Adding elements
matrix = np.append(matrix, [[10, 11, 12]], axis=0)
print(matrix)
# Output:
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]

# Removing elements
matrix = np.delete(matrix, 0, axis=0)
print(matrix)
# Output:
# [[ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]

# Modifying elements
matrix[0, 0] = 100
print(matrix)
# Output:
# [[100   5   6]
#  [  7   8   9]
#  [ 10  11  12]]
```

## 4. Operations on Multidimensional Arrays

### Indexing and Slicing

For 2D arrays, you can access rows, columns, or individual elements using indices.

```python
# Accessing a row
print(matrix[0])  # Output: [100   5   6]

# Accessing a column
print(matrix[:, 1])  # Output: [ 5  8 11]

# Accessing a specific element
print(matrix[1, 2])  # Output: 9
```

### Adding, Removing, and Modifying Elements

```python
# Adding a new row
new_row = np.array([[13, 14, 15]])
matrix = np.vstack([matrix, new_row])
print(matrix)
# Output:
# [[100   5   6]
#  [  7   8   9]
#  [ 10  11  12]
#  [ 13  14  15]]

# Adding a new column
new_col = np.array([[16], [17], [18], [19]])
matrix = np.hstack([matrix, new_col])
print(matrix)
# Output:
# [[100   5   6  16]
#  [  7   8   9  17]
#  [ 10  11  12  18]
#  [ 13  14  15  19]]

# Removing a row
matrix = np.delete(matrix, 1, axis=0)
print(matrix)
# Output:
# [[100   5   6  16]
#  [ 10  11  12  18]
#  [ 13  14  15  19]]

# Removing a column
matrix = np.delete(matrix, 2, axis=1)
print(matrix)
# Output:
# [[100   5  16]
#  [ 10  11  18]
#  [ 13  14  19]]
```

## 5. Common Array Functions and Methods

### List Methods

- `append()`: Adds an element to the end of the list.
- `remove()`: Removes the first occurrence of an element.
- `pop()`: Removes and returns the element at the given index.
- `sort()`: Sorts the list in ascending order.
- `reverse()`: Reverses the list.

### Numpy Array Functions

- `np.append()`: Appends values to the end of an array.
- `np.delete()`: Deletes elements from an array.
- `np.reshape()`: Reshapes an array.
- `np.transpose()`: Transposes the array.
- `np.sum()`: Returns the sum of array elements.

## 6. Excurse: Images

### Images as Arrays

Images can be represented as arrays, where each element corresponds to a pixel value. In Python, we can use the `PIL` (Pillow) library to work with images.

```python
from PIL import Image

# Load an image
img = Image.open('image.jpg')

# Convert the image to a numpy array
img_array = np.array(img)
print(img_array.shape)  # Output: (height, width, channels)
```

### Image Processing with Numpy

We can perform various image processing operations using numpy functions.

```python
# Convert the image to grayscale
gray_img = np.mean(img_array, axis=2)

# Resize the image
resized_img = np.resize(gray_img, (new_height, new_width))

# Apply a filter
filter = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
filtered_img = np.clip(np.convolve(gray_img, filter), 0, 255)
```

### Displaying Images

We can display images using matplotlib.

```python
import matplotlib.pyplot as plt

# Display the original image
plt.imshow(img_array)
plt.axis('off')
plt.show()

# Display the processed image
plt.imshow(filtered_img, cmap='gray')
plt.axis('off')
plt.show()
```

## Introduction to NumPy Arrays and Vectorized Operations

Let's compare the use of two nested for loops versus array calculations using NumPy for a simple task, such as adding two matrices.

### Example 1: Using Nested For Loops

We'll add two matrices using nested for loops.

```python
# Traditional nested loops method
import numpy as np

# Define two 3x3 matrices
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# Initialize an empty matrix to store the result
result = np.zeros((3, 3))

# Using nested for loops to add the matrices
for i in range(3):
    for j in range(3):
        result[i][j] = A[i][j] + B[i][j]

print("Result using nested loops:")
print(result)
```

### Example 2: Using Array Calculations (Vectorized Operations)

Now, let's do the same addition using NumPy's array operations, which is much faster and more concise.

```python
# Using NumPy's array operations
result_vectorized = A + B

print("Result using array calculation:")
print(result_vectorized)
```

### Explanation

1. **Nested For Loops**: In the first example, we manually iterate through each element of the matrices using two loops. This method is straightforward but can be slow for large matrices.

2. **Array Calculations**: In the second example, NumPy's array operations handle the element-wise addition automatically. This method is highly optimized and generally much faster, especially for large arrays.

### Output

Both methods will produce the same output:

```
Result using nested loops:v
[[10. 10. 10.]
 [10. 10. 10.]
 [10. 10. 10.]]

Result using array calculation:
[[10 10 10]
 [10 10 10]
 [10 10 10]]
```

The second method is more efficient and concise, making it preferable for most use cases involving array operations.y<>
