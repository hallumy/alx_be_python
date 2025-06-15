# Programming Paradigms & Exception Handling

## Introduction

This project explores two key areas of Python programming: Object-Oriented Programming (OOP) and Exception Handling. You will learn how to design structured, reusable code using classes and objects, and how to manage errors gracefully through exception handling techniques. Additionally, the project introduces basic testing practices to help ensure your code works as expected. By the end, you’ll have a strong foundation in building robust Python applications using OOP, custom error handling, and unit testing.

## Create a Simple Bank Account Class

This project consists of two Python scripts that simulate basic banking operations using Object-Oriented Programming (OOP) principles and command-line interaction.

bank_account.py
This file defines the BankAccount class, which models a simple bank account with the following features:

Attributes:

account_balance: stores the current balance (default is 0).

Methods:

deposit(amount): Adds the specified amount to the account.

withdraw(amount): Deducts the amount if sufficient funds are available; otherwise, returns False.

display_balance(): Prints the current account balance in a readable format.

Encapsulation is used to protect the account_balance attribute from direct access.

main-0.py
This script serves as the interface for users to interact with the BankAccount class via command-line arguments.

Usage Example:

bash
Copy
Edit
python3 main-0.py deposit:50
python3 main-0.py withdraw:20
python3 main-0.py display
Accepts one argument in the format: <command>:<amount> (e.g., deposit:100)

Commands:

deposit:<amount>

withdraw:<amount>

display

## Robust Division Calculator with Command Line Arguments

This project consists of two Python scripts that work together to perform division with robust error handling.

robust_division_calculator.py
Contains the function safe_divide(numerator, denominator) that safely performs division.

Handles:

Division by zero using ZeroDivisionError

Non-numeric input using ValueError

Converts inputs to float and returns either the result or an appropriate error message.

main.py
Provides a command-line interface.

Accepts two arguments: numerator and denominator.

Imports and uses safe_divide() to compute and print the result or error.
