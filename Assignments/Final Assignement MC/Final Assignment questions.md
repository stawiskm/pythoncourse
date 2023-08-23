# Assignment questions

**Variables and Arithmetic:**

1. What is the value of `x` after the following code is executed?

```python
x = 10
x = x + 5
```

   a) 10
   b) 15
   c) 5
   d) 25

**Functions and Getting Help:**

2. Which built-in function is used to get the length of a string or a list?

   a) `len()`
   b) `length()`
   c) `size()`
   d) `count()`

**Data Types:**

3. What data type is used to store a single, floating-point decimal number in Python?

   a) `int`
   b) `str`
   c) `float`
   d) `bool`

**Conditions and Conditional Statements:**

4. Which keyword is used to define the beginning of a block of code that is executed when a certain condition is true?

   a) `if`
   b) `when`
   c) `case`
   d) `check`

**Lists, Sets, and Dictionaries:**

5. Which data structure in Python is ordered, mutable, and allows duplicate elements?

   a) List
   b) Set
   c) Dictionary
   d) Tuple

**Loops: while and for, continue, break:**

6. In a `for` loop, what does the `break` statement do?

   a) Skips the rest of the loop and continues with the next iteration
   b) Ends the loop and continues with the next statement after the loop
   c) Skips the current iteration and continues with the next iteration
   d) Halts the program and raises an error

**Question 1:**
What is the purpose of using a logging framework in a software application?
a) To create graphical user interfaces (GUIs) for the application.
b) To retrieve data from APIs and external sources.
c) To manage and record information, errors, and events during runtime.
d) To generate random numbers and perform statistical calculations.

**Question 2:**
In software development, what is the primary role of a CSV (Comma-Separated Values) file?
a) To store graphical assets such as images and icons.
b) To define the layout and appearance of the user interface.
c) To store tabular data in a plain text format with rows and columns.
d) To execute complex mathematical operations and generate graphs.

**Question 3:**
What is the purpose of using the `matplotlib` library in Python programming?
a) To interact with external APIs and retrieve data.
b) To create and manipulate graphical user interfaces (GUIs).
c) To perform scientific and data visualization using graphs and plots.
d) To manage and control flow of execution in a program.

**Question 4:**
What is an API (Application Programming Interface)?
a) A graphical representation of a program's data flow.
b) A set of tools for creating graphical user interfaces (GUIs).
c) A collection of functions and protocols that allows different software applications to communicate with each other.
d) A database management system for organizing and querying data.

**Question 5:**
In software development, what does the term "GUI" stand for?
a) Global User Interaction
b) General Underlying Interface
c) Graphics and User Interface
d) Grouped User Instructions

**Question 6:**
What is the purpose of exception handling in programming?
a) To intentionally crash the program in case of an error.
b) To skip over errors and continue execution normally.
c) To provide additional functionality to the program.
d) To gracefully handle errors and prevent application crashes.

**Question 7:**
What does the term "API request" refer to?
a) A user's input in the graphical user interface.
b) A user's interaction with a button or widget.
c) A program's communication with an external service or resource over a network.
d) A program's execution of mathematical calculations.

**Question 1:**
What does the term "HTTP" stand for in the context of web communication?
a) Hyper Text Transfer Protocol
b) High Tech Transformation Process
c) Host Testing and Transfer Protocol
d) Hyperlink Textual Transfer Process

**Question 2:**
In Python, how can you make an HTTP GET request using the `requests` library?
a) `requests.post()`
b) `requests.get()`
c) `requests.put()`
d) `requests.retrieve()`

**Question 3:**
What is the purpose of the following code snippet?
```python
response = requests.get("http://api.example.com/data")
data = response.json()
```
a) It retrieves data from an API and stores it in a CSV file.
b) It generates random numbers for data visualization.
c) It sends a POST request to an external server.
d) It fetches JSON data from an API and stores it in the `data` variable.

**Question 4:**
Which library in Python is commonly used for data visualization and plotting?
a) `math`
b) `matplotlib`
c) `numpy`
d) `requests`

**Question 5:**
What is the purpose of a scatter plot in data visualization?
a) To show the distribution of a single variable.
b) To display the relationship between two variables.
c) To show the trend of a single variable over time.
d) To present categorical data in a bar chart.

**Question 6:**
What does the acronym "CSV" stand for in the context of data storage?
a) Compressed Statistical Values
b) Controlled Storage Vault
c) Comma-Separated Values
d) Categorical Statistical Variables

**Question 7:**
What is the purpose of the `Toplevel` widget in the `tkinter` library?
a) To create buttons and checkboxes.
b) To provide a top-level window for displaying additional content.
c) To manage logging and error messages.
d) To handle API requests.

**Question 8:**
What is the role of the `delete_button` in the code?
```python
delete_button = tk.Button(display_window, text="Delete", command=lambda i=i: delete_row(i, display_window))
```
a) To delete the entire `display_window`.
b) To remove a specific row from the displayed data.
c) To delete the data stored in the `data.csv` file.
d) To cancel the display of patient records.

**Question 9:**
What is the purpose of the `tight_layout()` method in `matplotlib`?
a) To adjust the spacing between subplots.
b) To calculate the BMI of a patient.
c) To generate random height and weight values.
d) To remove whitespace from the GUI interface.

**Question 10:**
What is the primary function of the `window.mainloop()` line in the code?
a) To execute API requests.
b) To generate random patient data.
c) To display the tkinter GUI window to the user.
d) To calculate and display the BMI of the patient.

**Question 11:**
What is a common use case for using a `Checkbutton` widget in a GUI?
a) Displaying textual information to the user.
b) Enabling users to make multiple selections from a list.
c) Providing a button to submit the form data.
d) Creating a navigation bar in the GUI.

**Question 12:**
What is the purpose of the `logger` object in the code?
a) To create random patient data.
b) To manage CSV files.
c) To retrieve data from APIs.
d) To log information, errors, and events during runtime.

**Question 13:**
How can you generate a random integer in the range of 1 to 100 using the `random` library?
a) `random.randint(1, 100)`
b) `random.random(1, 100)`
c) `random.choice(range(1, 100))`
d) `random.range(1, 100)`

**Question 14:**
In the context of programming, what is an "API key"?
a) A variable name used to store data.
b) A unique identifier used to label API requests.
c) A special function used to generate random numbers.
d) A type of graphical user interface element.

Question 1:
Which Pandas function is used to read a CSV file into a DataFrame?
A) `pd.import_csv('data.csv')`
B) `pd.read_csv('data.csv')`
C) `pd.load_csv('data.csv')`
D) `pd.open_csv('data.csv')`

Question 2:
What does the following code do?
```python
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df['C'] = df['A'] + df['B']
```
A) Creates a new DataFrame with columns 'A', 'B', and 'C'
B) Multiplies values in columns 'A' and 'B'
C) Divides values in columns 'A' and 'B'
D) Raises an error due to incorrect column assignment

Question 3:
How can you drop rows with missing values from a DataFrame `df`?
A) `df.drop_na()`
B) `df.remove_na()`
C) `df.dropna()`
D) `df.fillna()`

Question 4:
Which Pandas function is used to group data based on a specific column and apply aggregation functions?
A) `df.group()`
B) `df.aggregate()`
C) `df.groupby()`
D) `df.group_by()`

Question 5:
What does the following code do?
```python
df = df[df['column_name'] > 10]
```
A) Drops rows where 'column_name' is greater than 10
B) Replaces values in 'column_name' with 10 if they are greater
C) Adds 10 to each value in 'column_name'
D) Raises an error due to incorrect syntax

Question 6:
Which Pandas function is used to rename columns in a DataFrame?
A) `df.rename_columns()`
B) `df.columns_rename()`
C) `df.rename()`
D) `df.relabel_columns()`

Question 7:
What is the purpose of the `pd.concat()` function in Pandas?
A) It calculates the concatenation of two DataFrames.
B) It merges two DataFrames based on a common column.
C) It combines DataFrames vertically or horizontally.
D) It performs element-wise addition on two DataFrames.

Question 8:
How can you select specific rows and columns from a DataFrame `df` using their labels?
A) `df.select()`
B) `df.loc[]`
C) `df.iloc[]`
D) `df.filter()`

Question 9:
What does the `df.melt()` function do?
A) Melts the DataFrame into a Series.
B) Converts wide-format data to long-format.
C) Sorts the DataFrame rows in descending order.
D) Merges two DataFrames based on common columns.

Question 10:
Which function is used to pivot a DataFrame from long-format to wide-format?
A) `df.pivot()`
B) `df.reshape()`
C) `df.wide()`
D) `df.pivot_table()`

Question 11:
What does the following code do?
```python
df['new_column'] = df['existing_column'].apply(lambda x: x * 2)
```
A) Creates a new column 'new_column' with double the values of 'existing_column'.
B) Removes 'existing_column' from the DataFrame.
C) Applies the lambda function to each row of 'existing_column'.
D) Raises an error due to incorrect syntax.

Question 12:
How can you sort a DataFrame `df` based on values in a column 'column_name' in descending order?
A) `df.sort(column='column_name', ascending=False)`
B) `df.sort_values(by='column_name', ascending=False)`
C) `df.sort_by(column='column_name', order='desc')`
D) `df.order_values(by='column_name', ascending=False)`


**Question 1:**
```python
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22]}

df = pd.DataFrame(data)
result = df['Age'].sum()
print(result)
```
What will be the output of the code?

A) 77
B) 55
C) 25, 30, 22
D) 77.0

**Question 2:**
```python
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22]}

df = pd.DataFrame(data)
result = df[df['Age'] > 24]['Name']
print(result)
```
What will be the output of the code?

A) Alice, Bob, Charlie
B) Alice
C) Bob
D) Charlie

**Question 3:**
```python
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22]}

df = pd.DataFrame(data)
df['Age'] = df['Age'] + 5
result = df['Age'].mean()
print(result)
```
What will be the output of the code?

A) 25.0
B) 30.0
C) 27.33
D) 20.33

**Question 4:**
```python
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22]}

df = pd.DataFrame(data)
result = df.sort_values(by='Age', ascending=False)
print(result['Name'].iloc[0])
```
What will be the output of the code?

A) Alice
B) Bob
C) Charlie
D) Error

**Question 5:**
```python
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22]}

df = pd.DataFrame(data)
result = df.groupby('Age').count()
print(result['Name'].sum())
```
What will be the output of the code?

A) 3
B) 6
C) 2
D) 55

**Question 6:**
```python
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22]}

df = pd.DataFrame(data)
result = df['Name'].apply(lambda x: x.upper())
print(result)
```
What will be the output of the code?

A) ['ALICE', 'BOB', 'CHARLIE']
B) ALICE, BOB, CHARLIE
C) ['Alice', 'Bob', 'Charlie']
D) ['ALICE', BOB, 'CHARLIE']
