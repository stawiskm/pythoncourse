Write a Function that takes a list with three arguments and returns a string as a result. The first argument describes a number as a String (e.g., "eight"), the second argument describes another number as a String (e.g., "nine"), and the third argument describes the operation as a String (e.g., "plus") between the numbers. The result of this operation should be returned as written numbers (e.g., "seventeen"). The Function should test if the input is valid, and through an exception on division by zero.

```python

def perform_operation(args):
    number_map = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
        "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
        "eighteen": 18, "nineteen": 19, "twenty": 20
    }

    # Extracting the arguments
    num1, num2, operation = args

    # Validating the arguments
    if num1 not in number_map or num2 not in number_map:
        raise ValueError("Invalid number provided")

    # Converting numbers to integers
    num1, num2 = number_map[num1],number_map[num2]

    # Performing the operation
    if operation == "plus":
        result = num1 + num2
    elif operation == "minus":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        result = num1 / num2
    else:
        raise ValueError("Invalid operation provided")

    # Converting the result back to a string
    result_string = [key for key, value in number_map.items() if value == result]
    if len(result_string) == 0:
        raise ValueError("Invalid result")
    
    return result_string[0]


# Example usage:
input_list = ["eight", "nine", "plus"]
try:
    result = perform_operation(input_list)
    print(result)  # Output: "seventeen"
except (ValueError, ZeroDivisionError) as e:
    print(e)


```
