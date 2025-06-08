#!/usr/bin/env python

# A function that calculates two nummbers 

def perform_operation(num1, num2, operation):
    """
    Arguments:
              num1: First number(float)
              num2: Second number(float)
              operation: The operation to perform; add, subtract,multiply
                         or divide.
    Returns the operation performed.
    """ 
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            return num1 / num2
    else:
        return "Invalid operation. Please choose from 'add', 'subract', 'multiply' or 'divide'."   
